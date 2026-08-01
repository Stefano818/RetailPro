from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.sale import Sale


class SaleRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Sale]:
        statement = (
            select(Sale)
            .order_by(Sale.created_at.desc())
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        sale_id: int,
    ) -> Sale | None:

        statement = select(Sale).where(
            Sale.id == sale_id
        )

        return self.db.scalar(statement)

    def create(self, sale: Sale) -> Sale:
        self.db.add(sale)
        self.db.flush()

        return sale