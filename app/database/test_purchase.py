from decimal import Decimal

from app.database.session import SessionLocal

from app.repositories.product_repository import ProductRepository
from app.repositories.purchase_repository import PurchaseRepository
from app.repositories.stock_movement_repository import (
    StockMovementRepository,
)
from app.repositories.supplier_repository import SupplierRepository

from app.services.purchase_service import PurchaseService


def test_purchase():
    db = SessionLocal()

    try:
        product_repository = ProductRepository(db)
        purchase_repository = PurchaseRepository(db)
        supplier_repository = SupplierRepository(db)
        stock_movement_repository = (
            StockMovementRepository(db)
        )

        products = product_repository.get_active()

        if not products:
            print("No active products found.")
            return

        product = products[0]

        purchase_service = PurchaseService(
            db=db,
            purchase_repository=purchase_repository,
            product_repository=product_repository,
            supplier_repository=supplier_repository,
            stock_movement_repository=stock_movement_repository,
        )

        print("Product selected:")
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Stock before purchase: {product.stock}")

        purchase = purchase_service.create_purchase(
            supplier_id=1,
            user_id=1,
            items=[
                {
                    "product_id": product.id,
                    "quantity": Decimal("20"),
                    "unit_price": Decimal("8.00"),
                }
            ],
            tax=Decimal("0"),
            notes="Test purchase",
        )

        db.refresh(product)

        print()
        print("Purchase created successfully.")
        print(f"Purchase ID: {purchase.id}")
        print(f"Subtotal: {purchase.subtotal}")
        print(f"Tax: {purchase.tax}")
        print(f"Total: {purchase.total}")
        print(f"Stock after purchase: {product.stock}")

    except Exception as error:
        print()
        print("Purchase creation failed.")
        print(error)

    finally:
        db.close()


if __name__ == "__main__":
    test_purchase()