from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.stock_movement import StockMovement


class StockMovementRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[StockMovement]:
        statement = (
            select(StockMovement)
            .order_by(StockMovement.date.desc())
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        movement_id: int,
    ) -> StockMovement | None:

        statement = select(StockMovement).where(
            StockMovement.id == movement_id
        )

        return self.db.scalar(statement)

    def get_by_product(
        self,
        product_id: int,
    ) -> list[StockMovement]:

        statement = (
            select(StockMovement)
            .where(
                StockMovement.product_id == product_id
            )
            .order_by(StockMovement.date.desc())
        )

        return list(self.db.scalars(statement).all())

    def create(
        self,
        movement: StockMovement,
    ) -> StockMovement:

        self.db.add(movement)
        self.db.flush()

        return movement