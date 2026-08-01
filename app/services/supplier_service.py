from app.models.supplier import Supplier
from app.repositories.supplier_repository import SupplierRepository


class SupplierService:

    def __init__(self, repository: SupplierRepository):
        self.repository = repository

    def get_all(self) -> list[Supplier]:
        return self.repository.get_all()

    def get_by_id(self, supplier_id: int) -> Supplier:
        supplier = self.repository.get_by_id(supplier_id)

        if not supplier:
            raise ValueError("Supplier not found.")

        return supplier

    def create(
        self,
        legal_name: str,
        trade_name: str | None = None,
        tax_id: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        address: str | None = None,
        contact_name: str | None = None,
        notes: str | None = None,
    ) -> Supplier:

        legal_name = legal_name.strip()

        if not legal_name:
            raise ValueError(
                "Supplier legal name is required."
            )

        if tax_id:
            tax_id = tax_id.strip()

            if self.repository.get_by_tax_id(tax_id):
                raise ValueError(
                    "A supplier with this tax ID already exists."
                )

        supplier = Supplier(
            legal_name=legal_name,
            trade_name=(
                trade_name.strip()
                if trade_name
                else None
            ),
            tax_id=tax_id,
            phone=phone.strip() if phone else None,
            email=email.strip() if email else None,
            address=address.strip() if address else None,
            contact_name=(
                contact_name.strip()
                if contact_name
                else None
            ),
            notes=notes.strip() if notes else None,
        )

        return self.repository.create(supplier)

    def deactivate(self, supplier_id: int) -> Supplier:
        supplier = self.get_by_id(supplier_id)

        supplier.is_active = False

        return self.repository.update(supplier)