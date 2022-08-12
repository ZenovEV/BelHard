from http import HTTPStatus

from aiohttp import ClientSession
from sqlalchemy import select, update, delete
# from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from crud_old import articles
from models import create_async_session, Category, Article
from models.engine import create_client_session, Session, create_session
from schemas import CategoryInDBSema, CategorySchema, article
from schemas.article import ArticleInDBSchema, ArticleSchema


class CRUDArticle:

    @staticmethod
    @create_session
    async def add(user: ArticleSchema, session: AsyncSession = None, article =None) -> ArticleInDBSchema:
        article = Article(**article.dict())
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(user)
            return Article(**article.__dict__)

    @staticmethod
    @create_session
    async def get(user_id: int, session: AsyncSession = None) -> ArticleInDBSchema | list:
        article = await session.execute(
            select(Article)
            .where(Article.id == user_id)
        )
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article)
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_session
    async def get_all(parent_id: int = None, session: AsyncSession = None) -> ArticleSchema | list:
        if parent_id:
            articles = await session.execute(
                select(Article)
                .order_by(Article.id)
            )
        else:
            articles = await session.execute(
                select(Article)
                .order_by(Article.id)
            )
        return [ArticleSchema(**article[0].__dict__) for article in articles]


    @staticmethod
    @create_async_session
    async def update(
            category: CategoryInDBSema,
            session: AsyncSession = None

    ) -> bool:
        await session.execute(
            update(Article)
            .where(Article.id == article.id)
            .values(**category.dict())

        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    """@staticmethod
    @create_session
    async def get_articles(user_id: int, session: await AsyncSession = None) -> List[Tuple[User, Article]]:
        response = session.execute(
            select(User, Article)
            .join(Article, User.id == Article.category_id)
            .where(User.id == User)
        )
        return response.all()"""