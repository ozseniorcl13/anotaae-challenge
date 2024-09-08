from pydantic import BaseModel, Field


class CategoryResponseDTO(BaseModel):
    id: str
    title: str
    description: str
    owner_id: str
