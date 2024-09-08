from pydantic import BaseModel
from typing import Optional


class CategoryCreateDTO(BaseModel):
    title: str
    description: Optional[str]
    owner_id: str


class CategoryUpdateDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    owner_id: Optional[str]
