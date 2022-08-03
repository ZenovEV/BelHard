from sqlalchemy import Column, SmallInteger, VARCHAR, TIMESTAMP, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(24), unique=True, nullable=False)
    hashed_passord = Column(Text, nullable=False)
    is_blocked = Column(Boolean, default=False)

class Category(Base):
    __tablename__: str = "categories"
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(24), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))


class Article(Base):
    __tablename__: str = "articles"