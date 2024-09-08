from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    owner_id: str
