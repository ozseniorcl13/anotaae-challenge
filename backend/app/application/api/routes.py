from fastapi import APIRouter

from app.application.api.health_check.health_check_router import health_check_router
from app.application.api.product.product_router import product_router

api_routers = APIRouter(prefix="/v1")

api_routers.include_router(health_check_router)
api_routers.include_router(product_router)
