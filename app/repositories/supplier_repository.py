from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.models.supplier import Supplier


class SupplierRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(
        self,
        supplier: Supplier,
    ) -> Supplier:

        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)

        return supplier


    def get_all(self) -> list[Supplier]:

        statement = (
            select(Supplier)
            .order_by(Supplier.legal_name)
        )

        return list(self.db.scalars(statement).all())

    def get_active(self) -> list[Supplier]:

        statement = (
            select(Supplier)
            .where(Supplier.is_active.is_(True))
            .order_by(Supplier.legal_name)
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        supplier_id: int,
    ) -> Supplier | None:

        statement = (
            select(Supplier)
            .where(Supplier.id == supplier_id)
        )

        return self.db.scalar(statement)

    def get_by_tax_id(
        self,
        tax_id: str,
    ) -> Supplier | None:

        statement = (
            select(Supplier)
            .where(Supplier.tax_id == tax_id)
        )

        return self.db.scalar(statement)

    def get_by_legal_name(
        self,
        legal_name: str,
    ) -> Supplier | None:

        statement = (
            select(Supplier)
            .where(Supplier.legal_name == legal_name)
        )

        return self.db.scalar(statement)

    def get_by_trade_name(
        self,
        trade_name: str,
    ) -> Supplier | None:

        statement = (
            select(Supplier)
            .where(Supplier.trade_name == trade_name)
        )

        return self.db.scalar(statement)

    def search(
        self,
        search_term: str,
    ) -> list[Supplier]:

        statement = (
            select(Supplier)
            .where(
                or_(
                    Supplier.legal_name.ilike(f"%{search_term}%"),
                    Supplier.trade_name.ilike(f"%{search_term}%"),
                    Supplier.tax_id.ilike(f"%{search_term}%"),
                    Supplier.contact_name.ilike(f"%{search_term}%"),
                )
            )
            .order_by(Supplier.legal_name)
        )

        return list(self.db.scalars(statement).all())


    def update(
        self,
        supplier: Supplier,
    ) -> Supplier:

        self.db.commit()
        self.db.refresh(supplier)

        return supplier


    def delete(
        self,
        supplier: Supplier,
    ) -> Supplier:

        supplier.is_active = False

        self.db.commit()
        self.db.refresh(supplier)

        return supplier

    def restore(
        self,
        supplier: Supplier,
    ) -> Supplier:

        supplier.is_active = True

        self.db.commit()
        self.db.refresh(supplier)

        return supplier


    def exists_tax_id(
        self,
        tax_id: str,
    ) -> bool:

        return self.get_by_tax_id(tax_id) is not None

    def exists_legal_name(
        self,
        legal_name: str,
    ) -> bool:

        return self.get_by_legal_name(legal_name) is not None

    def count(self) -> int:

        statement = (
            select(func.count(Supplier.id))
        )

        return self.db.scalar(statement) or 0