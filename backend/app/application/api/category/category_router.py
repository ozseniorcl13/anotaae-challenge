from fastapi import APIRouter, Depends

from app.application.api.category.schema.category_request import CategoryRequest
from app.application.api.category.schema.category_response import CategoryResponse
from app.application.dependencies.dependencies import get_category_service
from app.domain.category.service.category_service import CategoryService


category_router = APIRouter(
    prefix="/categories",
    tags=["Category"],
)


@category_router.post(
    "", summary="Create a category", status_code=200, response_model=CategoryResponse
)
async def create(
    request: CategoryRequest,
    category_service: CategoryService = Depends(get_category_service),
):
    category_data = request.dict()
    return await category_service.create_category(category_data)
