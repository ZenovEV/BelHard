from http import HTTPStatus

from aiohttp import ClientSession
from sqlalchemy import select, update, delete
# from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Category
from models.engine import create_client_session
from schemas import CategoryInDBSema, CategorySchema


class ClientSession:

    @staticmethod
    @create_client_session
    async def get_add_article(session: ClientSession = None) -> dict:
        response = await session.get(
            url="/api/1/article/add",
            json=(
                {
                    "title": "string",
                    "body": "string",
                    "category_id": 1,
                    "user_id": 1
                }
            )
        )
        if response.status == HTTPStatus.OK:
            return await response.json()


    @staticmethod
    @create_client_session
    async def get_article(session: ClientSession = None,
                          article_id: int = None
    ) -> dict:
        params = {}
        if article_id:
            params['article_id'] = article_id
        response = await session.get(
            url="/api/1/article/get",
            params=params,
            json=(
                {
                    "title": "string",
                    "body": "string",
                    "category_id": 1,
                    "user_id": 1,
                    "id": 1
                }
            )

        )
        if response.status == HTTPStatus.OK:
            return await response.json()

    @staticmethod
    @create_client_session
    async def get_all(
            session: ClientSession = None,
            category_id: int = None) -> dict:
        params = {}
        if category_id:
            params['category_id'] = category_id
        response = await session.get(
            url="/api/1/article/all",
            params=params
        )
        if response.status == HTTPStatus.OK:
            return await response.json()








class CRUDCategory:

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> CategoryInDBSema | None:
        category = await session.execute(
            select(Category).where(Category.id == category_id)
            .where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return CategoryInDBSema(**category[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(parent_id: int = None, session: AsyncSession = None) -> CategoryInDBSema | list:
        if parent_id:
            categories = await session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = await session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [CategoryInDBSema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_async_session
    async def add(category: CategorySchema, session: AsyncSession = None) -> CategoryInDBSema | None:
        category = Category(**category.dict())
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(category)
            return CategoryInDBSema(**category.__dict__)

    @staticmethod
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            category: CategoryInDBSema,
            session: AsyncSession = None

    ) -> bool:
        await session.execute(
            update(Category)
            .where(Category.id == category.id)
            .values(**category.dict())

        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True


'''
    @staticmethod
    @create_async_session
    async def get_articles(category_id: int, session=None) -> list[tuple[Category, Article]]:
        restponse = session.execute(
            select(Category, Article)
            .join(Article, Category.id == Article.category_id)
            .where(Category.id == category_id)

        )
        return restponse.all()

'''
