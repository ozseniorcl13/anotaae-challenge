from typing import List
from bson import ObjectId
from app.application.api.product.dto.product_request import (
    ProductCreateDTO,
    ProductUpdateDTO,
)
from app.application.api.product.dto.product_response import ProductResponseDTO
from app.domain.product.entity.product import Product
from app.domain.product.exception.product_exception import (
    ProductNotFoundException,
    InvalidIdException,
)
from app.domain.product.repository.product_repository import ProductRepository
from app.domain.category.service.category_service import CategoryService


class ProductService:
    def __init__(
        self, product_repository: ProductRepository, category_service: CategoryService
    ):
        self.product_repository = product_repository
        self.category_service = category_service

    async def create(self, product_data: ProductCreateDTO) -> ProductResponseDTO:
        if not ObjectId.is_valid(product_data.category_id):
            raise InvalidIdException(product_data.category_id)

        category = await self.category_service.get_by_id(product_data.category_id)

        product = Product(**product_data.dict())
        created_product = await self.product_repository.create(product)

        return ProductResponseDTO(
            id=created_product.id,
            title=created_product.title,
            description=created_product.description,
            price=created_product.price,
            category=category,
            owner_id=created_product.owner_id,
        )

    async def get_all(self) -> List[ProductResponseDTO]:
        products = await self.product_repository.get_all()
        return [
            ProductResponseDTO(
                id=product.id,
                title=product.title,
                description=product.description,
                price=product.price,
                category=await self.category_service.get_by_id(product.category_id),
                owner_id=product.owner_id,
            )
            for product in products
        ]

    async def get_by_id(self, id: str) -> ProductResponseDTO:
        if not ObjectId.is_valid(id):
            raise InvalidIdException(id)

        product = await self.product_repository.get_by_id(id)
        if not product:
            raise ProductNotFoundException(id)

        return ProductResponseDTO(
            id=product.id,
            title=product.title,
            description=product.description,
            price=product.price,
            category=await self.category_service.get_by_id(product.category_id),
            owner_id=product.owner_id,
        )

    async def update(
        self, id: str, product_data: ProductUpdateDTO
    ) -> ProductResponseDTO:
        if not ObjectId.is_valid(id):
            raise InvalidIdException(id)

        product = await self.product_repository.get_by_id(id)
        if not product:
            raise ProductNotFoundException(id)

        product.update_values(product_data.dict(exclude_unset=True))
        updated_product = await self.product_repository.update(id, product)

        return ProductResponseDTO(
            id=updated_product.id,
            title=updated_product.title,
            description=updated_product.description,
            price=updated_product.price,
            category=await self.category_service.get_by_id(updated_product.category_id),
            owner_id=updated_product.owner_id,
        )

    async def delete(self, id: str):
        if not ObjectId.is_valid(id):
            raise InvalidIdException(id)

        product = await self.product_repository.get_by_id(id)
        if not product:
            raise ProductNotFoundException(id)

        await self.product_repository.delete(id)
