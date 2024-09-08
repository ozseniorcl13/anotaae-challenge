from typing import List

from app.domain.category.entity.category import Category
from app.domain.category.repository.category_repository import \
    CategoryRepository
from app.infra.database.mongo.document.category_document import \
    CategoryDocument


class CategoryRepositoryImpl(CategoryRepository):

    async def create(self, category: Category) -> Category:
        category_doc = CategoryDocument(**category.dict())
        await category_doc.insert()
        return Category(**category_doc.dict())

    async def get_all(self) -> List[Category]:
        category_docs = await CategoryDocument.find_all().to_list()
        return [Category(**category_doc.dict()) for category_doc in category_docs]

    async def get_by_id(self, id: str) -> Category:
        category_doc = await CategoryDocument.get(id)
        if category_doc:
            return Category(**category_doc.dict())
        return None

    async def update(self, id: str, category: Category) -> Category:
        category_doc = await CategoryDocument.get(id)
        await category_doc.set(category.dict())
        return Category(**category_doc.dict())

    async def delete(self, id: str) -> bool:
        category_doc = await CategoryDocument.get(id)
        await category_doc.delete()
