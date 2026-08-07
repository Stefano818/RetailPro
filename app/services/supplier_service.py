from app.models.supplier import Supplier
from app.repositories.supplier_repository import SupplierRepository


class SupplierService:

    def __init__(
        self,
        supplier_repository: SupplierRepository,
    ):
        self.supplier_repository = supplier_repository


    def get_all(self) -> list[Supplier]:
        return self.supplier_repository.get_all()

    def get_active(self) -> list[Supplier]:
        return self.supplier_repository.get_active()

    def count(self) -> int:
        return self.supplier_repository.count()

    def search(
        self,
        search_term: str,
    ) -> list[Supplier]:

        search_term = search_term.strip()

        if not search_term:
            return self.get_active()

        return self.supplier_repository.search(search_term)

    def get_by_id(
        self,
        supplier_id: int,
    ) -> Supplier:

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

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
                "Legal name is required."
            )

        if self.supplier_repository.exists_legal_name(
            legal_name
        ):
            raise ValueError(
                "Supplier already exists."
            )

        if tax_id:

            tax_id = tax_id.strip()

            if self.supplier_repository.exists_tax_id(
                tax_id
            ):
                raise ValueError(
                    "Tax ID already exists."
                )

        supplier = Supplier(
            legal_name=legal_name,
            trade_name=trade_name.strip() if trade_name else None,
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

        return self.supplier_repository.create(
            supplier
        )


    def update(
        self,
        supplier_id: int,
        legal_name: str,
        trade_name: str | None = None,
        tax_id: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        address: str | None = None,
        contact_name: str | None = None,
        notes: str | None = None,
    ) -> Supplier:

        supplier = self.get_by_id(supplier_id)

        legal_name = legal_name.strip()

        if not legal_name:
            raise ValueError(
                "Legal name is required."
            )

        existing = (
            self.supplier_repository.get_by_legal_name(
                legal_name
            )
        )

        if (
            existing
            and existing.id != supplier.id
        ):
            raise ValueError(
                "Supplier already exists."
            )

        if tax_id:

            tax_id = tax_id.strip()

            existing_tax = (
                self.supplier_repository.get_by_tax_id(
                    tax_id
                )
            )

            if (
                existing_tax
                and existing_tax.id != supplier.id
            ):
                raise ValueError(
                    "Tax ID already exists."
                )

        supplier.legal_name = legal_name
        supplier.trade_name = (
            trade_name.strip()
            if trade_name
            else None
        )
        supplier.tax_id = tax_id
        supplier.phone = (
            phone.strip()
            if phone
            else None
        )
        supplier.email = (
            email.strip()
            if email
            else None
        )
        supplier.address = (
            address.strip()
            if address
            else None
        )
        supplier.contact_name = (
            contact_name.strip()
            if contact_name
            else None
        )
        supplier.notes = (
            notes.strip()
            if notes
            else None
        )

        return self.supplier_repository.update(
            supplier
        )

    def deactivate(
        self,
        supplier_id: int,
    ) -> Supplier:

        supplier = self.get_by_id(
            supplier_id
        )

        return self.supplier_repository.delete(
            supplier
        )

    def restore(
        self,
        supplier_id: int,
    ) -> Supplier:

        supplier = self.get_by_id(
            supplier_id
        )

        return self.supplier_repository.restore(
            supplier
        )