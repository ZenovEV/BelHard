from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, TIMESTAMP, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(24), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    is_blocked = Column(Boolean, default=False)
    email = Column(Text, unique=True)


class Category(Base):
    __tablename__: str = "categories"
    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))




class Article(Base):
    __tablename__: str = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(45), nullable=False)
    body = Column(VARCHAR(1024), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    category_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    autor_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)


class ArticleComments(Base):
    __table__: str = "article_comments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    article_id = Column(Integer, ForeignKey ("articles.id", ondelete="CASCADE"), nullable=False)
    comment = Column(VARCHAR(140), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())

"""
class UserArticle(Base):
    __tablename__: str = "user_articles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="NO ACTION"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
"""