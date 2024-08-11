from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: str
    title: str
    description: str
    owner_id: str
