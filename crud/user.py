from typing import Optional, List, Tuple

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import create_session, User, Article

from schemas.user import UserInDBSchema, UserSchema


class CRUDUser:

    @staticmethod
    @create_session
    def add(user: UserSchema, session: Session = None) -> UserInDBSchema:
        user = User(**user.dict())
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(user)
            return User(**user.__dict__)

    @staticmethod
    @create_session
    def get(user_id: int, session: Session = None) -> UserInDBSchema | list:
        user = session.execute(
            select(User)
            .where(User.id == user_id)
        )
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(user)
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> UserInDBSchema | list:
        if parent_id:
            users = session.execute(
                select(User)
                .order_by(User.id)
            )
        else:
            categories = session.execute(
                select(User)
                .order_by(User.id)
            )
        return [UserInDBSchema(**user[0].__dict__) for user in users]

    @staticmethod
    @create_session
    def update(
            user: UserInDBSchema,
            session: Session = None
    ) -> bool:
        session.execute(
            update(User)
            .where(User.id == User.id)
            .values(**user.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def get_articles(user_id: int, session: Session = None) -> List[Tuple[User, Article]]:
        response = session.execute(
            select(User, Article)
            .join(Article, User.id == Article.category_id)
            .where(User.id == User)
        )
        return response.all()
