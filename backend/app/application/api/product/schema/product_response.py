from pydantic import BaseModel
from app.application.api.category.schema.category_response import CategoryResponse


class ProductResponse(BaseModel):
    id: str
    title: str
    description: str
    price: float
    category: CategoryResponse
    owner_id: str
