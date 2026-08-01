from app.models.category import Category
from app.repositories.category_repository import CategoryRepository


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def get_all(self) -> list[Category]:
        return self.repository.get_all()

    def get_by_id(self, category_id: int) -> Category:
        category = self.repository.get_by_id(category_id)

        if not category:
            raise ValueError("Category not found.")

        return category

    def create(
        self,
        name: str,
        description: str | None = None,
    ) -> Category:

        name = name.strip()

        if not name:
            raise ValueError("Category name is required.")

        existing_category = self.repository.get_by_name(name)

        if existing_category:
            raise ValueError(
                "A category with this name already exists."
            )

        category = Category(
            name=name,
            description=description.strip()
            if description
            else None,
        )

        return self.repository.create(category)

    def update(
        self,
        category_id: int,
        name: str,
        description: str | None = None,
    ) -> Category:

        category = self.get_by_id(category_id)

        name = name.strip()

        if not name:
            raise ValueError("Category name is required.")

        existing_category = self.repository.get_by_name(name)

        if (
            existing_category
            and existing_category.id != category_id
        ):
            raise ValueError(
                "A category with this name already exists."
            )

        category.name = name
        category.description = (
            description.strip()
            if description
            else None
        )

        return self.repository.update(category)

    def deactivate(self, category_id: int) -> Category:
        category = self.get_by_id(category_id)

        category.is_active = False

        return self.repository.update(category)