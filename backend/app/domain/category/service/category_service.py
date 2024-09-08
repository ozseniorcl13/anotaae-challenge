from app.application.api.category.dto.category_request import (
    CategoryCreateDTO,
)
from app.application.api.category.dto.category_response import CategoryResponseDTO
from app.domain.category.model.category import Category
from app.domain.category.repository.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def create(self, category_data: CategoryCreateDTO) -> CategoryResponseDTO:
        category = Category(**category_data.dict())
        created_category = await self.category_repository.create(category)
        return CategoryResponseDTO(**created_category.dict())
