from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Customer]:
        statement = select(Customer).order_by(Customer.id)

        return list(self.db.scalars(statement).all())

    def get_by_id(self, customer_id: int) -> Customer | None:
        statement = select(Customer).where(
            Customer.id == customer_id
        )

        return self.db.scalar(statement)

    def get_by_dni(self, dni: str) -> Customer | None:
        statement = select(Customer).where(
            Customer.dni == dni
        )

        return self.db.scalar(statement)

    def create(self, customer: Customer) -> Customer:
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)

        return customer

    def update(self, customer: Customer) -> Customer:
        self.db.commit()
        self.db.refresh(customer)

        return customer

    def delete(self, customer: Customer) -> None:
        self.db.delete(customer)
        self.db.commit()