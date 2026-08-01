from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Product]:
        statement = select(Product).order_by(Product.name)

        return list(self.db.scalars(statement).all())

    def get_active(self) -> list[Product]:
        statement = (
            select(Product)
            .where(Product.is_active.is_(True))
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(self, product_id: int) -> Product | None:
        statement = select(Product).where(
            Product.id == product_id
        )

        return self.db.scalar(statement)

    def get_by_code(self, code: str) -> Product | None:
        statement = select(Product).where(
            Product.code == code
        )

        return self.db.scalar(statement)

    def get_by_barcode(self, barcode: str) -> Product | None:
        statement = select(Product).where(
            Product.barcode == barcode
        )

        return self.db.scalar(statement)

    def get_low_stock(self) -> list[Product]:
        statement = (
            select(Product)
            .where(
                Product.stock <= Product.minimum_stock,
                Product.is_active.is_(True),
            )
            .order_by(Product.stock)
        )

        return list(self.db.scalars(statement).all())

    def create(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

        return product

    def update(self, product: Product) -> Product:
        self.db.commit()
        self.db.refresh(product)

        return product

    def delete(self, product: Product) -> None:
        self.db.delete(product)
        self.db.commit()