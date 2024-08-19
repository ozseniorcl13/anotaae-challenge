from fastapi import APIRouter, Depends


from app.application.api.product.schema.product_request import ProductRequest
from app.application.api.product.schema.product_response import ProductResponse
from app.application.dependencies.dependencies import get_product_service
from app.domain.product.service.product_service import ProductService

product_router = APIRouter(
    prefix="/products",
    tags=["Product"],
)


@product_router.post(
    "", summary="Create a product", status_code=200, response_model=ProductResponse
)
async def create(
    request: ProductRequest,
    product_service: ProductService = Depends(get_product_service),
):
    product_data = request.dict()
    return await product_service.create_product(product_data)


@product_router.get(
    "/{product_id}",
    summary="Get a product",
    status_code=200,
    response_model=ProductResponse,
)
async def get(
    product_id: str,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.get_product_by_id(product_id)
