from datetime import datetime, time
from decimal import Decimal

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.customer import Customer
from app.models.supplier import Supplier
from app.models.user import User
from app.models.sale import Sale
from app.models.purchase import Purchase


class DashboardService:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db




    def get_total_products(self) -> int:

        statement = (
            select(func.count(Product.id))
            .where(
                Product.is_active.is_(True)
            )
        )

        return self.db.scalar(statement) or 0


    def get_total_customers(self) -> int:

        statement = (
            select(func.count(Customer.id))
            .where(
                Customer.is_active.is_(True)
            )
        )

        return self.db.scalar(statement) or 0


    def get_total_suppliers(self) -> int:

        statement = (
            select(func.count(Supplier.id))
            .where(
                Supplier.is_active.is_(True)
            )
        )

        return self.db.scalar(statement) or 0


    def get_total_users(self) -> int:

        statement = (
            select(func.count(User.id))
            .where(
                User.is_active.is_(True)
            )
        )

        return self.db.scalar(statement) or 0



    def get_low_stock_products(self) -> list[Product]:

        statement = (
            select(Product)
            .where(
                Product.stock <= Product.minimum_stock,
                Product.is_active.is_(True),
            )
            .order_by(Product.stock)
        )

        return list(
            self.db.scalars(statement).all()
        )


    def get_low_stock_count(self) -> int:

        statement = (
            select(func.count(Product.id))
            .where(
                Product.stock <= Product.minimum_stock,
                Product.is_active.is_(True),
            )
        )

        return self.db.scalar(statement) or 0


    def get_inventory_value(self) -> Decimal:

        statement = select(
            func.sum(
                Product.stock *
                Product.purchase_price
            )
        )

        return (
            self.db.scalar(statement)
            or Decimal("0")
        )



    def get_sales_today(self) -> Decimal:

        today = datetime.today().date()

        start = datetime.combine(
            today,
            time.min
        )

        end = datetime.combine(
            today,
            time.max
        )

        statement = (
            select(
                func.sum(Sale.total)
            )
            .where(
                Sale.date >= start,
                Sale.date <= end,
            )
        )

        return (
            self.db.scalar(statement)
            or Decimal("0")
        )


    def get_sales_count_today(self) -> int:

        today = datetime.today().date()

        start = datetime.combine(
            today,
            time.min
        )

        end = datetime.combine(
            today,
            time.max
        )

        statement = (
            select(
                func.count(Sale.id)
            )
            .where(
                Sale.date >= start,
                Sale.date <= end,
            )
        )

        return self.db.scalar(statement) or 0




    def get_purchases_today(self) -> Decimal:

        today = datetime.today().date()

        start = datetime.combine(
            today,
            time.min
        )

        end = datetime.combine(
            today,
            time.max
        )

        statement = (
            select(
                func.sum(Purchase.total)
            )
            .where(
                Purchase.date >= start,
                Purchase.date <= end,
            )
        )

        return (
            self.db.scalar(statement)
            or Decimal("0")
        )


    def get_dashboard_summary(self):

        return {

            "products":
                self.get_total_products(),

            "customers":
                self.get_total_customers(),

            "suppliers":
                self.get_total_suppliers(),

            "users":
                self.get_total_users(),

            "low_stock":
                self.get_low_stock_count(),

            "inventory_value":
                self.get_inventory_value(),

            "sales_today":
                self.get_sales_today(),

            "sales_count_today":
                self.get_sales_count_today(),

            "purchases_today":
                self.get_purchases_today(),
        }