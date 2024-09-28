from typing import List

from fastapi import APIRouter, Depends, status

from app.application.api.product.dto.product_request import (ProductCreateDTO,
                                                             ProductUpdateDTO)
from app.application.api.product.dto.product_response import ProductResponseDTO
from app.application.dependencies.dependencies import get_product_service
from app.domain.product.service.product_service import ProductService

product_router = APIRouter(
    prefix="/products",
    tags=["Product"],
)


@product_router.post(
    "",
    summary="Create a product",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponseDTO,
)
async def create(
    product_data: ProductCreateDTO,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.create(product_data)


@product_router.get(
    "",
    summary="Get all products",
    status_code=status.HTTP_200_OK,
    response_model=List[ProductResponseDTO],
)
async def get_all(
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.get_all()


@product_router.get(
    "/{id}",
    summary="Get a product",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponseDTO,
)
async def get_one(
    id: str,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.get_by_id(id)


@product_router.patch(
    "",
    summary="Update a product",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponseDTO,
)
async def update(
    id: str,
    product_data: ProductUpdateDTO,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.update(id, product_data)


@product_router.delete(
    "",
    summary="Delete a product",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    id: str,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.delete(id)
