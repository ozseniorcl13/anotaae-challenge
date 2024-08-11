from fastapi import APIRouter

from app.application.api.product.schema.product_request import ProductRequest

product_router = APIRouter(
    prefix="/products",
    tags=["Product"],
)


@product_router.post(
    "",
    summary="Create a product",
    status_code=200,
)
async def create(request: ProductRequest):
    pass
