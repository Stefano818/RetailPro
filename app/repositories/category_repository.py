from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, category: Category) -> Category:
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category


    def get_all(self) -> list[Category]:
        statement = (
            select(Category)
            .order_by(Category.name)
        )

        return list(self.db.scalars(statement).all())

    def get_active(self) -> list[Category]:
        statement = (
            select(Category)
            .where(Category.is_active.is_(True))
            .order_by(Category.name)
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        category_id: int,
    ) -> Category | None:

        statement = (
            select(Category)
            .where(Category.id == category_id)
        )

        return self.db.scalar(statement)

    def get_by_name(
        self,
        name: str,
    ) -> Category | None:

        statement = (
            select(Category)
            .where(Category.name == name)
        )

        return self.db.scalar(statement)

    def search(
        self,
        search_term: str,
    ) -> list[Category]:

        statement = (
            select(Category)
            .where(
                or_(
                    Category.name.ilike(f"%{search_term}%"),
                    Category.description.ilike(f"%{search_term}%"),
                )
            )
            .order_by(Category.name)
        )

        return list(self.db.scalars(statement).all())


    def update(
        self,
        category: Category,
    ) -> Category:

        self.db.commit()
        self.db.refresh(category)

        return category



    def delete(
        self,
        category: Category,
    ) -> Category:

        category.is_active = False

        self.db.commit()
        self.db.refresh(category)

        return category

    def restore(
        self,
        category: Category,
    ) -> Category:

        category.is_active = True

        self.db.commit()
        self.db.refresh(category)

        return category



    def exists_name(
        self,
        name: str,
    ) -> bool:

        return self.get_by_name(name) is not None



    def count(self) -> int:

        statement = select(
            func.count(Category.id)
        )

        return self.db.scalar(statement) or 0