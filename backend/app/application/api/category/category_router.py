from typing import List

from fastapi import APIRouter, Depends, status

from app.application.api.category.dto.category_request import (
    CategoryCreateDTO, CategoryUpdateDTO)
from app.application.api.category.dto.category_response import \
    CategoryResponseDTO
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


@category_router.get(
    "",
    summary="Get all categories",
    status_code=status.HTTP_200_OK,
    response_model=List[CategoryResponseDTO],
)
async def get_all(
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.get_all()


@category_router.get(
    "/{id}",
    summary="Get one category",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponseDTO,
)
async def get_one(
    id: str,
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.get_by_id(id)


@category_router.patch(
    "",
    summary="Update a category",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponseDTO,
)
async def update(
    id: str,
    category_data: CategoryUpdateDTO,
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.update(id, category_data)


@category_router.delete(
    "",
    summary="Delete a category",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    id: str,
    category_service: CategoryService = Depends(get_category_service),
):
    return await category_service.delete(id)
