from app.domain.category.model.category import Category
from app.domain.category.repository.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def create_category(self, category_data: dict) -> Category:
        category = Category(**category_data)
        return await self.category_repository.create(category)
