from http import HTTPStatus

from aiohttp import ClientSession
#from sqlalchemy import select, update, delete
# from sqlalchemy.orm import Session
#from sqlalchemy.exc import IntegrityError
#from sqlalchemy.ext.asyncio import AsyncSession

#from models import create_async_session, Category
from models.engine import create_client_session
#from schemas import CategoryInDBSema, CategorySchema


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
                          article_id: int = None) -> dict:
        params = {}
        if article_id:
            params['article_id'] = article_id
        response = await session.get(
            url="/api/1/article/get",
            params=params,

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







