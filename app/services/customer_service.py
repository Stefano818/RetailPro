from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(
        self,
        customer_repository: CustomerRepository,
    ):
        self.customer_repository = customer_repository


    def get_all(self) -> list[Customer]:

        return self.customer_repository.get_all()

    def get_active(self) -> list[Customer]:

        return self.customer_repository.get_active()

    def count(self) -> int:

        return self.customer_repository.count()

    def search(
        self,
        search_term: str,
    ) -> list[Customer]:

        search_term = search_term.strip()

        if not search_term:
            return self.get_active()

        return self.customer_repository.search(
            search_term
        )

    def get_by_id(
        self,
        customer_id: int,
    ) -> Customer:

        customer = (
            self.customer_repository.get_by_id(
                customer_id
            )
        )

        if not customer:
            raise ValueError(
                "Customer not found."
            )

        return customer


    def create(
        self,
        name: str,
        phone: str | None = None,
        email: str | None = None,
        dni: str | None = None,
    ) -> Customer:

        name = name.strip()

        if not name:
            raise ValueError(
                "Customer name is required."
            )

        if dni:

            dni = dni.strip()

            if self.customer_repository.exists_dni(
                dni
            ):
                raise ValueError(
                    "DNI already exists."
                )

        if email:

            email = email.strip()

            if self.customer_repository.exists_email(
                email
            ):
                raise ValueError(
                    "Email already exists."
                )

        customer = Customer(
            name=name,
            phone=(
                phone.strip()
                if phone
                else None
            ),
            email=email,
            dni=dni,
        )

        return self.customer_repository.create(
            customer
        )


    def update(
        self,
        customer_id: int,
        name: str,
        phone: str | None = None,
        email: str | None = None,
        dni: str | None = None,
    ) -> Customer:

        customer = self.get_by_id(
            customer_id
        )

        name = name.strip()

        if not name:
            raise ValueError(
                "Customer name is required."
            )

        if dni:

            dni = dni.strip()

            existing_dni = (
                self.customer_repository.get_by_dni(
                    dni
                )
            )

            if (
                existing_dni
                and existing_dni.id != customer.id
            ):
                raise ValueError(
                    "DNI already exists."
                )

        if email:

            email = email.strip()

            existing_email = (
                self.customer_repository.get_by_email(
                    email
                )
            )

            if (
                existing_email
                and existing_email.id != customer.id
            ):
                raise ValueError(
                    "Email already exists."
                )

        customer.name = name
        customer.phone = (
            phone.strip()
            if phone
            else None
        )
        customer.email = email
        customer.dni = dni

        return self.customer_repository.update(
            customer
        )


    def deactivate(
        self,
        customer_id: int,
    ) -> Customer:

        customer = self.get_by_id(
            customer_id
        )

        return self.customer_repository.delete(
            customer
        )

    def restore(
        self,
        customer_id: int,
    ) -> Customer:

        customer = self.get_by_id(
            customer_id
        )

        return self.customer_repository.restore(
            customer
        )