from fastapi import Depends

from app.domain.category.service.category_service import CategoryService
from app.infra.database.mongo.mongodb_client import MongoDBClient
from app.infra.repository.product_repository_impl import ProductRepositoryImpl
from app.infra.repository.category_repository_impl import \
    CategoryRepositoryImpl
from app.domain.product.service.product_service import ProductService

# def get_mongo_client() -> MongoDBClient:
#     return MongoDBClient()


def get_product_repository(
    # mongo_client: MongoDBClient = Depends(get_mongo_client),
) -> ProductRepositoryImpl:
    return ProductRepositoryImpl()


def get_category_repository(
    # mongo_client: MongoDBClient = Depends(get_mongo_client),
) -> CategoryRepositoryImpl:
    return CategoryRepositoryImpl()


def get_category_service(
    category_repository: CategoryRepositoryImpl = Depends(get_category_repository),
) -> CategoryService:
    return CategoryService(category_repository)


def get_product_service(
    product_repository: ProductRepositoryImpl = Depends(get_product_repository),
    category_service: CategoryRepositoryImpl = Depends(get_category_service),
) -> ProductService:
    return ProductService(product_repository, category_service)
