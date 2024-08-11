from fastapi import Depends

from app.domain.product.service.product_service import ProductService
from app.infra.database.mongo.mongodb_client import MongoDBClient
from app.infra.repository.product_repository_impl import ProductRepositoryImpl


def get_mongo_client() -> MongoDBClient:
    return MongoDBClient()


def get_product_repository(
    mongo_client: MongoDBClient = Depends(get_mongo_client),
) -> ProductRepositoryImpl:
    return ProductRepositoryImpl(mongo_client)


def get_product_service(
    product_repository: ProductRepositoryImpl = Depends(get_product_repository),
) -> ProductService:
    return ProductService(product_repository)
