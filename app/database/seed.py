from decimal import Decimal

from sqlalchemy import func, select

from app.database.session import SessionLocal

from app.models.category import Category
from app.models.product import Product
from app.models.supplier import Supplier
from app.models.user import User


def seed_database():
    db = SessionLocal()

    try:
        # =========================================================
        # USER
        # =========================================================

        admin = db.scalar(
            select(User).where(
                User.email == "admin@retailpro.com"
            )
        )

        if not admin:
            admin = User(
                name="System Administrator",
                dni="00000001",
                email="admin@retailpro.com",
                password_hash="demo_password_hash",
                role="admin",
                is_active=True,
            )

            db.add(admin)
            db.flush()

        # =========================================================
        # SUPPLIER
        # =========================================================

        supplier = db.scalar(
            select(Supplier).where(
                Supplier.tax_id == "30700000001"
            )
        )

        if not supplier:
            supplier = Supplier(
                legal_name="RetailPro Supplier S.A.",
                trade_name="RetailPro Supplier",
                tax_id="30700000001",
                phone="3515555555",
                email="supplier@retailpro.com",
                address="Argentina",
                contact_name="Sales Department",
                notes="Demo supplier for RetailPro.",
                is_active=True,
            )

            db.add(supplier)
            db.flush()

        # =========================================================
        # CATEGORIES
        # =========================================================

        categories_data = [
            {
                "name": "Clothing",
                "description": (
                    "Clothing and apparel products."
                ),
            },
            {
                "name": "Electronics",
                "description": (
                    "Electronic devices and accessories."
                ),
            },
            {
                "name": "Accessories",
                "description": (
                    "General accessories and complementary products."
                ),
            },
        ]

        categories = {}

        for data in categories_data:

            category = db.scalar(
                select(Category).where(
                    Category.name == data["name"]
                )
            )

            if not category:
                category = Category(
                    name=data["name"],
                    description=data["description"],
                    is_active=True,
                )

                db.add(category)
                db.flush()

            categories[data["name"]] = category

        # =========================================================
        # PRODUCTS
        # =========================================================

        products_data = [
            {
                "code": "TSHIRT-BLK-001",
                "barcode": "779000000001",
                "name": "Basic Black T-Shirt",
                "brand": "RetailPro",
                "description": (
                    "Basic black cotton t-shirt."
                ),
                "category": "Clothing",
                "purchase_price": Decimal("8.00"),
                "retail_price": Decimal("15.00"),
                "wholesale_price": Decimal("12.00"),
                "wholesale_min_quantity": Decimal("10"),
                "stock": Decimal("50"),
                "minimum_stock": Decimal("10"),
                "unit": "unit",
            },
            {
                "code": "JEANS-BLU-001",
                "barcode": "779000000002",
                "name": "Classic Blue Jeans",
                "brand": "RetailPro",
                "description": (
                    "Classic blue denim jeans."
                ),
                "category": "Clothing",
                "purchase_price": Decimal("20.00"),
                "retail_price": Decimal("38.00"),
                "wholesale_price": Decimal("32.00"),
                "wholesale_min_quantity": Decimal("5"),
                "stock": Decimal("25"),
                "minimum_stock": Decimal("5"),
                "unit": "unit",
            },
            {
                "code": "MOUSE-WRL-001",
                "barcode": "779000000003",
                "name": "Wireless Mouse",
                "brand": "TechPro",
                "description": (
                    "Wireless optical mouse."
                ),
                "category": "Electronics",
                "purchase_price": Decimal("7.50"),
                "retail_price": Decimal("15.00"),
                "wholesale_price": Decimal("12.50"),
                "wholesale_min_quantity": Decimal("10"),
                "stock": Decimal("40"),
                "minimum_stock": Decimal("8"),
                "unit": "unit",
            },
            {
                "code": "HEADPHONES-001",
                "barcode": "779000000004",
                "name": "Wireless Headphones",
                "brand": "TechPro",
                "description": (
                    "Wireless Bluetooth headphones."
                ),
                "category": "Electronics",
                "purchase_price": Decimal("18.00"),
                "retail_price": Decimal("35.00"),
                "wholesale_price": Decimal("30.00"),
                "wholesale_min_quantity": Decimal("5"),
                "stock": Decimal("18"),
                "minimum_stock": Decimal("5"),
                "unit": "unit",
            },
            {
                "code": "BACKPACK-BLK-001",
                "barcode": "779000000005",
                "name": "Black Backpack",
                "brand": "RetailPro",
                "description": (
                    "Everyday black backpack."
                ),
                "category": "Accessories",
                "purchase_price": Decimal("12.00"),
                "retail_price": Decimal("25.00"),
                "wholesale_price": Decimal("21.00"),
                "wholesale_min_quantity": Decimal("8"),
                "stock": Decimal("30"),
                "minimum_stock": Decimal("6"),
                "unit": "unit",
            },
        ]

        products_created = 0

        for data in products_data:

            existing_product = db.scalar(
                select(Product).where(
                    Product.code == data["code"]
                )
            )

            if existing_product:
                continue

            product = Product(
                code=data["code"],
                barcode=data["barcode"],
                name=data["name"],
                brand=data["brand"],
                description=data["description"],
                category_id=categories[
                    data["category"]
                ].id,
                supplier_id=supplier.id,
                purchase_price=data["purchase_price"],
                retail_price=data["retail_price"],
                wholesale_price=data["wholesale_price"],
                wholesale_min_quantity=(
                    data["wholesale_min_quantity"]
                ),
                stock=data["stock"],
                minimum_stock=data["minimum_stock"],
                unit=data["unit"],
                image=None,
                is_active=True,
            )

            db.add(product)
            products_created += 1

        # =========================================================
        # COMMIT
        # =========================================================

        db.commit()

        # =========================================================
        # SUMMARY
        # =========================================================

        product_count = db.scalar(
            select(func.count(Product.id))
        )

        category_count = db.scalar(
            select(func.count(Category.id))
        )

        print()
        print("=" * 50)
        print("RetailPro database seed completed successfully.")
        print("=" * 50)
        print()
        print(f"Admin user ID: {admin.id}")
        print(f"Supplier ID: {supplier.id}")
        print(f"Products created: {products_created}")
        print(f"Total products: {product_count}")
        print(f"Total categories: {category_count}")
        print()
        print("Demo credentials:")
        print("Email: admin@retailpro.com")
        print("Password: demo_password")
        print()
        print("=" * 50)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()