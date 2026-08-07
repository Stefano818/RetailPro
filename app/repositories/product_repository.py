from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

        return product


    def get_all(self) -> list[Product]:
        statement = (
            select(Product)
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())

    def get_active(self) -> list[Product]:
        statement = (
            select(Product)
            .where(Product.is_active.is_(True))
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        product_id: int,
    ) -> Product | None:

        statement = (
            select(Product)
            .where(Product.id == product_id)
        )

        return self.db.scalar(statement)

    def get_by_code(
        self,
        code: str,
    ) -> Product | None:

        statement = (
            select(Product)
            .where(Product.code == code)
        )

        return self.db.scalar(statement)

    def get_by_barcode(
        self,
        barcode: str,
    ) -> Product | None:

        statement = (
            select(Product)
            .where(Product.barcode == barcode)
        )

        return self.db.scalar(statement)

    def search(
        self,
        search_term: str,
    ) -> list[Product]:

        statement = (
            select(Product)
            .where(
                or_(
                    Product.name.ilike(f"%{search_term}%"),
                    Product.code.ilike(f"%{search_term}%"),
                    Product.brand.ilike(f"%{search_term}%"),
                )
            )
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())


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

    def get_out_of_stock(self) -> list[Product]:
        statement = (
            select(Product)
            .where(
                Product.stock <= 0,
                Product.is_active.is_(True),
            )
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())

    def get_by_category(
        self,
        category_id: int,
    ) -> list[Product]:

        statement = (
            select(Product)
            .where(
                Product.category_id == category_id,
                Product.is_active.is_(True),
            )
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())

    def get_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Product]:

        statement = (
            select(Product)
            .where(
                Product.supplier_id == supplier_id,
                Product.is_active.is_(True),
            )
            .order_by(Product.name)
        )

        return list(self.db.scalars(statement).all())


    def update(
        self,
        product: Product,
    ) -> Product:

        self.db.commit()
        self.db.refresh(product)

        return product


    def delete(
        self,
        product: Product,
    ) -> Product:

        product.is_active = False

        self.db.commit()
        self.db.refresh(product)

        return product

    def restore(
        self,
        product: Product,
    ) -> Product:

        product.is_active = True

        self.db.commit()
        self.db.refresh(product)

        return product


    def exists_code(
        self,
        code: str,
    ) -> bool:

        return self.get_by_code(code) is not None

    def exists_barcode(
        self,
        barcode: str,
    ) -> bool:

        return self.get_by_barcode(barcode) is not None



    def count(self) -> int:

        statement = select(
            func.count(Product.id)
        )

        return self.db.scalar(statement) or 0