from app.domain.category.repository.category_repository import CategoryRepository
from app.domain.category.model.category import Category

from app.infra.database.mongo.document.category_document import CategoryDocument


class CategoryRepositoryImpl(CategoryRepository):

    async def create(self, category: Category) -> Category:
        # category_doc = CategoryDocument(**category.dict())
        # await category_doc.insert()
        category_doc = CategoryDocument(**category.dict())
        await category_doc.insert()
        print("************************************** impleeee")
        print(category_doc.dict())
        return Category(**category_doc.dict())
