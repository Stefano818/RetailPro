from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.purchase import Purchase


class PurchaseRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Purchase]:
        statement = (
            select(Purchase)
            .order_by(Purchase.date.desc())
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        purchase_id: int,
    ) -> Purchase | None:

        statement = select(Purchase).where(
            Purchase.id == purchase_id
        )

        return self.db.scalar(statement)

    def create(
        self,
        purchase: Purchase,
    ) -> Purchase:

        self.db.add(purchase)
        self.db.flush()

        return purchase