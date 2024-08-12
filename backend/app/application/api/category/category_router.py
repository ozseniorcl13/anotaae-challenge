from typing import List
from fastapi import APIRouter, Depends, status

from app.application.api.category.schema.category_request import CategoryRequest
from app.application.api.category.schema.category_response import CategoryResponse
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
    response_model=CategoryResponse,
)
async def create(
    request: CategoryRequest,
    category_service: CategoryService = Depends(get_category_service),
):
    category_data = request.dict()
    return await category_service.create_category(category_data)


@category_router.get(
    "",
    summary="Get all categories",
    status_code=status.HTTP_200_OK,
    response_model=List[CategoryResponse],
)
async def get_all(
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.get_all_categories()


@category_router.get(
    "/{category_id}",
    summary="Get a category",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponse,
)
async def get(
    category_id: str,
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.get_category_by_id(category_id)


@category_router.delete(
    "/{category_id}",
    summary="Delete a category",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponse,
)
async def delete(
    category_id: str,
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.delete_category(category_id)


@category_router.patch(
    "/{category_id}",
    summary="Update a category",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponse,
)
async def delete(
    category_id: str,
    request: CategoryRequest,
    category_service: CategoryService = Depends(get_category_service),
):
    category_data = request.dict()
    return await category_service.update_category(category_id, category_data)
