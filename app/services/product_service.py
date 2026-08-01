from decimal import Decimal

from app.models.product import Product
from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.supplier_repository import SupplierRepository


class ProductService:

    def __init__(
        self,
        product_repository: ProductRepository,
        category_repository: CategoryRepository,
        supplier_repository: SupplierRepository,
    ):
        self.product_repository = product_repository
        self.category_repository = category_repository
        self.supplier_repository = supplier_repository

    def get_all(self) -> list[Product]:
        return self.product_repository.get_all()

    def get_active(self) -> list[Product]:
        return self.product_repository.get_active()

    def get_low_stock(self) -> list[Product]:
        return self.product_repository.get_low_stock()

    def get_by_id(self, product_id: int) -> Product:
        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise ValueError("Product not found.")

        return product

    def _validate_prices(
        self,
        purchase_price: Decimal,
        retail_price: Decimal,
        wholesale_price: Decimal | None,
    ) -> None:

        if purchase_price < 0:
            raise ValueError(
                "Purchase price cannot be negative."
            )

        if retail_price <= 0:
            raise ValueError(
                "Retail price must be greater than zero."
            )

        if retail_price < purchase_price:
            raise ValueError(
                "Retail price cannot be lower than purchase price."
            )

        if wholesale_price is not None:

            if wholesale_price <= 0:
                raise ValueError(
                    "Wholesale price must be greater than zero."
                )

            if wholesale_price < purchase_price:
                raise ValueError(
                    "Wholesale price cannot be lower "
                    "than purchase price."
                )

    def _validate_wholesale(
        self,
        wholesale_price: Decimal | None,
        wholesale_min_quantity: Decimal | None,
    ) -> None:

        if wholesale_price is not None:
            if (
                wholesale_min_quantity is None
                or wholesale_min_quantity <= 0
            ):
                raise ValueError(
                    "Wholesale minimum quantity is required "
                    "when wholesale price is configured."
                )

        if wholesale_min_quantity is not None:
            if wholesale_min_quantity <= 0:
                raise ValueError(
                    "Wholesale minimum quantity must "
                    "be greater than zero."
                )

    def create(
        self,
        code: str,
        name: str,
        category_id: int,
        purchase_price: Decimal,
        retail_price: Decimal,
        unit: str,
        supplier_id: int | None = None,
        barcode: str | None = None,
        brand: str | None = None,
        description: str | None = None,
        wholesale_price: Decimal | None = None,
        wholesale_min_quantity: Decimal | None = None,
        stock: Decimal = Decimal("0"),
        minimum_stock: Decimal = Decimal("0"),
        image: str | None = None,
    ) -> Product:

        code = code.strip()
        name = name.strip()
        unit = unit.strip()

        if not code:
            raise ValueError("Product code is required.")

        if not name:
            raise ValueError("Product name is required.")

        if not unit:
            raise ValueError("Product unit is required.")

        if self.product_repository.get_by_code(code):
            raise ValueError(
                "A product with this code already exists."
            )

        if barcode:
            barcode = barcode.strip()

            if self.product_repository.get_by_barcode(barcode):
                raise ValueError(
                    "A product with this barcode already exists."
                )

        category = self.category_repository.get_by_id(category_id)

        if not category:
            raise ValueError("Category not found.")

        if not category.is_active:
            raise ValueError(
                "Cannot assign an inactive category."
            )

        if supplier_id is not None:
            supplier = self.supplier_repository.get_by_id(
                supplier_id
            )

            if not supplier:
                raise ValueError("Supplier not found.")

            if not supplier.is_active:
                raise ValueError(
                    "Cannot assign an inactive supplier."
                )

        self._validate_prices(
            purchase_price,
            retail_price,
            wholesale_price,
        )

        self._validate_wholesale(
            wholesale_price,
            wholesale_min_quantity,
        )

        if stock < 0:
            raise ValueError(
                "Stock cannot be negative."
            )

        if minimum_stock < 0:
            raise ValueError(
                "Minimum stock cannot be negative."
            )

        product = Product(
            code=code,
            barcode=barcode,
            name=name,
            brand=brand.strip() if brand else None,
            description=(
                description.strip()
                if description
                else None
            ),
            category_id=category_id,
            supplier_id=supplier_id,
            purchase_price=purchase_price,
            retail_price=retail_price,
            wholesale_price=wholesale_price,
            wholesale_min_quantity=wholesale_min_quantity,
            stock=stock,
            minimum_stock=minimum_stock,
            unit=unit,
            image=image,
        )

        return self.product_repository.create(product)

    def deactivate(self, product_id: int) -> Product:
        product = self.get_by_id(product_id)

        product.is_active = False

        return self.product_repository.update(product)