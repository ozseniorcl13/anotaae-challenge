from fastapi import APIRouter, Depends, status

from app.application.api.category.dto.category_request import CategoryCreateDTO
from app.application.api.category.dto.category_response import CategoryResponseDTO
from app.application.dependencies.dependencies import get_category_service
from app.domain.category.service.category_service import CategoryService


category_router = APIRouter(
    prefix="/categories",
    tags=["Category"],
)


@category_router.post(
    "",
    summary="Create a category",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryResponseDTO,
)
async def create(
    category_data: CategoryCreateDTO,
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.create(category_data)
