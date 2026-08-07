from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_detail import SaleDetail

from app.repositories.customer_repository import CustomerRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.sale_repository import SaleRepository


class SaleService:

    def __init__(
        self,
        db: Session,
        sale_repository: SaleRepository,
        product_repository: ProductRepository,
        customer_repository: CustomerRepository,
        inventory_service,
    ):
        self.db = db
        self.sale_repository = sale_repository
        self.product_repository = product_repository
        self.customer_repository = customer_repository
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



    def _get_unit_price(
        self,
        product: Product,
        quantity: Decimal,
    ) -> Decimal:

        if (
            product.wholesale_price is not None
            and product.wholesale_min_quantity is not None
            and quantity >= product.wholesale_min_quantity
        ):
            return product.wholesale_price

        return product.retail_price



    def create_sale(
        self,
        customer_id: int | None,
        user_id: int,
        items: list[dict],
        discount: Decimal = Decimal("0"),
        payment_method: str = "cash",
    ) -> Sale:


        if not items:
            raise ValueError(
                "A sale must contain at least one product."
            )


        if discount < 0:
            raise ValueError(
                "Discount cannot be negative."
            )


        allowed_payment_methods = {
            "cash",
            "debit_card",
            "credit_card",
            "bank_transfer",
            "other",
        }


        if payment_method not in allowed_payment_methods:
            raise ValueError(
                "Invalid payment method."
            )



        if customer_id is not None:

            customer = (
                self.customer_repository
                .get_by_id(customer_id)
            )


            if not customer:
                raise ValueError(
                    "Customer not found."
                )


            if not customer.is_active:
                raise ValueError(
                    "Customer is inactive."
                )


        try:

            with self.db.begin():


                sale = Sale(

                    customer_id=customer_id,

                    user_id=user_id,

                    subtotal=Decimal("0"),

                    discount=discount,

                    total=Decimal("0"),

                    payment_method=payment_method,
                )


                self.db.add(
                    sale
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


                    if quantity <= 0:

                        raise ValueError(
                            "Product quantity must be greater than zero."
                        )



                    product = self._get_product(
                        product_id
                    )



                    if not self.inventory_service.has_stock(
                        product.id,
                        quantity,
                    ):

                        raise ValueError(
                            f"Insufficient stock for "
                            f"product '{product.name}'."
                        )



                    unit_price = self._get_unit_price(
                        product,
                        quantity,
                    )



                    line_total = (
                        unit_price * quantity
                    )



                    detail = SaleDetail(

                        sale_id=sale.id,

                        product_id=product.id,

                        quantity=quantity,

                        unit_price=unit_price,

                        subtotal=line_total,
                    )


                    self.db.add(
                        detail
                    )



                    self.inventory_service.decrease_stock(

                        product_id=product.id,

                        quantity=quantity,

                        user_id=user_id,

                        movement_type="sale",

                        reason="Product sold",

                        reference=f"SALE-{sale.id}",
                    )



                    subtotal += line_total



                total = subtotal - discount



                if total < 0:

                    raise ValueError(
                        "Discount cannot be greater than subtotal."
                    )



                sale.subtotal = subtotal

                sale.total = total



            self.db.refresh(
                sale
            )


            return sale



        except Exception:

            raise