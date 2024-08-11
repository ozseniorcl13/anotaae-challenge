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
    print(product_data)
    return await product_service.create_product(product_data)
