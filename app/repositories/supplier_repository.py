from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.supplier import Supplier


class SupplierRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Supplier]:
        statement = select(Supplier).order_by(Supplier.legal_name)

        return list(self.db.scalars(statement).all())

    def get_by_id(self, supplier_id: int) -> Supplier | None:
        statement = select(Supplier).where(
            Supplier.id == supplier_id
        )

        return self.db.scalar(statement)

    def get_by_tax_id(self, tax_id: str) -> Supplier | None:
        statement = select(Supplier).where(
            Supplier.tax_id == tax_id
        )

        return self.db.scalar(statement)

    def create(self, supplier: Supplier) -> Supplier:
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)

        return supplier

    def update(self, supplier: Supplier) -> Supplier:
        self.db.commit()
        self.db.refresh(supplier)

        return supplier

    def delete(self, supplier: Supplier) -> None:
        self.db.delete(supplier)
        self.db.commit()