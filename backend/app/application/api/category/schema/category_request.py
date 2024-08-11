from pydantic import BaseModel


class CategoryRequest(BaseModel):
    title: str
    description: str
    owner_id: str
