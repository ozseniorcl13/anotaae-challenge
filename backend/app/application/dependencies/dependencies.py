from fastapi import Depends

from app.domain.category.service.category_service import CategoryService
from app.domain.product.service.product_service import ProductService
from app.infra.aws.ssm.ssm_service import SSMService, ssm_service
from app.infra.repository.category_repository_impl import \
    CategoryRepositoryImpl
from app.infra.repository.product_repository_impl import ProductRepositoryImpl


def get_ssm_service() -> SSMService:
    return ssm_service()


def get_product_repository() -> ProductRepositoryImpl:
    return ProductRepositoryImpl()


def get_category_repository() -> CategoryRepositoryImpl:
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
