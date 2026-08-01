from app.database.database import engine
from app.models.base_model import Base

from app.models import (
    User,
    Customer,
    Supplier,
    Category,
    Product,
    Sale,
    SaleDetail,
    Purchase,
    PurchaseDetail,
    StockMovement,
)


def init_database():
    Base.metadata.create_all(bind=engine)
    print("Database created successfully.")


if __name__ == "__main__":
    init_database()