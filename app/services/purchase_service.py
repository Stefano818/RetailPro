from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.purchase import Purchase
from app.models.purchase_detail import PurchaseDetail

from app.repositories.product_repository import ProductRepository
from app.repositories.purchase_repository import PurchaseRepository
from app.repositories.supplier_repository import SupplierRepository


class PurchaseService:

    def __init__(
        self,
        db: Session,
        purchase_repository: PurchaseRepository,
        product_repository: ProductRepository,
        supplier_repository: SupplierRepository,
        inventory_service,
    ):
        self.db = db
        self.purchase_repository = purchase_repository
        self.product_repository = product_repository
        self.supplier_repository = supplier_repository
        self.inventory_service = inventory_service



    def _get_product(
        self,
        product_id: int,
    ) -> Product:

        product = self.product_repository.get_by_id(
            product_id
        )

        if not product:
            raise ValueError(
                f"Product {product_id} not found."
            )

        if not product.is_active:
            raise ValueError(
                f"Product {product.name} is inactive."
            )

        return product



    def create_purchase(
        self,
        supplier_id: int,
        user_id: int,
        items: list[dict],
        tax: Decimal = Decimal("0"),
        notes: str | None = None,
    ) -> Purchase:


        if not items:
            raise ValueError(
                "A purchase must contain at least one product."
            )


        if tax < 0:
            raise ValueError(
                "Tax cannot be negative."
            )


        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )


        if not supplier:
            raise ValueError(
                "Supplier not found."
            )


        if not supplier.is_active:
            raise ValueError(
                "Supplier is inactive."
            )


        try:

            with self.db.begin():

                purchase = Purchase(

                    supplier_id=supplier_id,

                    user_id=user_id,

                    subtotal=Decimal("0"),

                    tax=tax,

                    total=Decimal("0"),

                    status="completed",

                    notes=notes,
                )


                self.db.add(
                    purchase
                )


                self.db.flush()


                subtotal = Decimal("0")


                for item in items:


                    product_id = item.get(
                        "product_id"
                    )


                    quantity = Decimal(
                        str(
                            item.get(
                                "quantity",
                                0
                            )
                        )
                    )


                    unit_price = Decimal(
                        str(
                            item.get(
                                "unit_price",
                                0
                            )
                        )
                    )


                    if quantity <= 0:

                        raise ValueError(
                            "Purchase quantity must be greater than zero."
                        )


                    if unit_price <= 0:

                        raise ValueError(
                            "Purchase unit price must be greater than zero."
                        )


                    product = self._get_product(
                        product_id
                    )


                    line_total = (
                        quantity * unit_price
                    )


                    detail = PurchaseDetail(

                        purchase_id=purchase.id,

                        product_id=product.id,

                        quantity=quantity,

                        unit_price=unit_price,

                        subtotal=line_total,
                    )


                    self.db.add(
                        detail
                    )


                    self.inventory_service.increase_stock(

                        product_id=product.id,

                        quantity=quantity,

                        user_id=user_id,

                        movement_type="purchase",

                        reason="Product purchased",

                        reference=f"PURCHASE-{purchase.id}",
                    )


                    subtotal += line_total



                total = subtotal + tax


                purchase.subtotal = subtotal

                purchase.total = total



            self.db.refresh(
                purchase
            )


            return purchase



        except Exception:

            raise