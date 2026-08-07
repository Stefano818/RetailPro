from app.models.category import Category
from app.repositories.category_repository import CategoryRepository


class CategoryService:

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self.category_repository = category_repository


    def get_all(self) -> list[Category]:
        return self.category_repository.get_all()

    def get_active(self) -> list[Category]:
        return self.category_repository.get_active()

    def count(self) -> int:
        return self.category_repository.count()

    def search(
        self,
        search_term: str,
    ) -> list[Category]:

        search_term = search_term.strip()

        if not search_term:
            return self.get_active()

        return self.category_repository.search(search_term)

    def get_by_id(
        self,
        category_id: int,
    ) -> Category:

        category = self.category_repository.get_by_id(category_id)

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

        if self.category_repository.exists_name(name):
            raise ValueError("Category already exists.")

        category = Category(
            name=name,
            description=description.strip() if description else None,
        )

        return self.category_repository.create(category)


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

        existing = self.category_repository.get_by_name(name)

        if existing and existing.id != category.id:
            raise ValueError("Category already exists.")

        category.name = name
        category.description = (
            description.strip() if description else None
        )

        return self.category_repository.update(category)

    def deactivate(
        self,
        category_id: int,
    ) -> Category:

        category = self.get_by_id(category_id)

        return self.category_repository.delete(category)

    def restore(
        self,
        category_id: int,
    ) -> Category:

        category = self.get_by_id(category_id)

        return self.category_repository.restore(category)