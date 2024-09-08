from pydantic import BaseModel

from app.application.api.category.dto.category_response import CategoryResponseDTO


class ProductResponseDTO(BaseModel):
    id: str
    title: str
    description: str
    price: float
    category: CategoryResponseDTO
    owner_id: str
