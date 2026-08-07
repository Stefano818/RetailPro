from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.stock_movement import StockMovement

from app.repositories.product_repository import ProductRepository


class InventoryService:

    def __init__(
        self,
        db: Session,
        product_repository: ProductRepository,
    ):
        self.db = db
        self.product_repository = product_repository


    def get_product_stock(
        self,
        product_id: int,
    ) -> Decimal:

        product = self._get_product(
            product_id
        )

        return product.stock


    def increase_stock(
        self,
        product_id: int,
        quantity: Decimal,
        user_id: int,
        movement_type: str,
        reason: str | None = None,
        reference: str | None = None,
    ) -> Product:


        if quantity <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )


        product = self._get_product(
            product_id
        )


        previous_stock = product.stock


        product.stock += quantity


        self._create_movement(
            product=product,
            user_id=user_id,
            movement_type=movement_type,
            quantity=quantity,
            previous_stock=previous_stock,
            reason=reason,
            reference=reference,
        )


        return product


    def decrease_stock(
        self,
        product_id: int,
        quantity: Decimal,
        user_id: int,
        movement_type: str,
        reason: str | None = None,
        reference: str | None = None,
    ) -> Product:


        if quantity <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )


        product = self._get_product(
            product_id
        )


        if product.stock < quantity:

            raise ValueError(
                "Insufficient stock."
            )


        previous_stock = product.stock


        product.stock -= quantity


        self._create_movement(
            product=product,
            user_id=user_id,
            movement_type=movement_type,
            quantity=quantity,
            previous_stock=previous_stock,
            reason=reason,
            reference=reference,
        )


        return product



    def adjust_stock(
        self,
        product_id: int,
        new_quantity: Decimal,
        user_id: int,
        reason: str,
    ) -> Product:


        if new_quantity < 0:

            raise ValueError(
                "Stock cannot be negative."
            )


        product = self._get_product(
            product_id
        )


        previous_stock = product.stock


        difference = (
            new_quantity - previous_stock
        )


        product.stock = new_quantity


        self._create_movement(
            product=product,
            user_id=user_id,
            movement_type="adjustment",
            quantity=abs(difference),
            previous_stock=previous_stock,
            reason=reason,
        )


        return product


    def has_stock(
        self,
        product_id: int,
        quantity: Decimal,
    ) -> bool:

        product = self._get_product(
            product_id
        )

        return product.stock >= quantity



    def _create_movement(
        self,
        product: Product,
        user_id: int,
        movement_type: str,
        quantity: Decimal,
        previous_stock: Decimal,
        reason: str | None = None,
        reference: str | None = None,
    ) -> StockMovement:


        movement = StockMovement(

            product_id=product.id,

            user_id=user_id,

            movement_type=movement_type,

            quantity=quantity,

            previous_stock=previous_stock,

            new_stock=product.stock,

            reason=reason,

            reference=reference,
        )


        self.db.add(
            movement
        )


        return movement



    def _get_product(
        self,
        product_id: int,
    ) -> Product:


        product = (
            self.product_repository
            .get_by_id(product_id)
        )


        if not product:

            raise ValueError(
                "Product not found."
            )


        return product