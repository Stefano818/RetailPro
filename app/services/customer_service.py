from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def get_all(self) -> list[Customer]:
        return self.repository.get_all()

    def get_by_id(self, customer_id: int) -> Customer:
        customer = self.repository.get_by_id(customer_id)

        if not customer:
            raise ValueError("Customer not found.")

        return customer

    def create(
        self,
        name: str,
        phone: str | None = None,
        email: str | None = None,
        dni: str | None = None,
        address: str | None = None,
        notes: str | None = None,
    ) -> Customer:

        name = name.strip()

        if not name:
            raise ValueError("Customer name is required.")

        if dni:
            dni = dni.strip()

            if self.repository.get_by_dni(dni):
                raise ValueError(
                    "A customer with this DNI already exists."
                )

        customer = Customer(
            name=name,
            phone=phone.strip() if phone else None,
            email=email.strip() if email else None,
            dni=dni,
            address=address.strip() if address else None,
            notes=notes.strip() if notes else None,
        )

        return self.repository.create(customer)

    def deactivate(self, customer_id: int) -> Customer:
        customer = self.get_by_id(customer_id)

        customer.is_active = False

        return self.repository.update(customer)