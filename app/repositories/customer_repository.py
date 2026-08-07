from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(
        self,
        customer: Customer,
    ) -> Customer:

        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)

        return customer


    def get_all(self) -> list[Customer]:

        statement = (
            select(Customer)
            .order_by(Customer.name)
        )

        return list(
            self.db.scalars(statement).all()
        )

    def get_active(self) -> list[Customer]:

        statement = (
            select(Customer)
            .where(
                Customer.is_active.is_(True)
            )
            .order_by(Customer.name)
        )

        return list(
            self.db.scalars(statement).all()
        )

    def get_by_id(
        self,
        customer_id: int,
    ) -> Customer | None:

        statement = (
            select(Customer)
            .where(
                Customer.id == customer_id
            )
        )

        return self.db.scalar(statement)

    def get_by_dni(
        self,
        dni: str,
    ) -> Customer | None:

        statement = (
            select(Customer)
            .where(
                Customer.dni == dni
            )
        )

        return self.db.scalar(statement)

    def get_by_email(
        self,
        email: str,
    ) -> Customer | None:

        statement = (
            select(Customer)
            .where(
                Customer.email == email
            )
        )

        return self.db.scalar(statement)

    def search(
        self,
        search_term: str,
    ) -> list[Customer]:

        statement = (
            select(Customer)
            .where(
                or_(
                    Customer.name.ilike(
                        f"%{search_term}%"
                    ),
                    Customer.dni.ilike(
                        f"%{search_term}%"
                    ),
                    Customer.email.ilike(
                        f"%{search_term}%"
                    ),
                    Customer.phone.ilike(
                        f"%{search_term}%"
                    ),
                )
            )
            .order_by(Customer.name)
        )

        return list(
            self.db.scalars(statement).all()
        )


    def update(
        self,
        customer: Customer,
    ) -> Customer:

        self.db.commit()
        self.db.refresh(customer)

        return customer


    def delete(
        self,
        customer: Customer,
    ) -> Customer:

        customer.is_active = False

        self.db.commit()
        self.db.refresh(customer)

        return customer

    def restore(
        self,
        customer: Customer,
    ) -> Customer:

        customer.is_active = True

        self.db.commit()
        self.db.refresh(customer)

        return customer


    def exists_dni(
        self,
        dni: str,
    ) -> bool:

        return self.get_by_dni(dni) is not None

    def exists_email(
        self,
        email: str,
    ) -> bool:

        return self.get_by_email(email) is not None


    def count(self) -> int:

        statement = select(
            func.count(Customer.id)
        )

        return self.db.scalar(statement) or 0