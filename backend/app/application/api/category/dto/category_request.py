from typing import Optional

from pydantic import BaseModel


class CategoryCreateDTO(BaseModel):
    title: str
    description: Optional[str]
    owner_id: str


class CategoryUpdateDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[str] = None
