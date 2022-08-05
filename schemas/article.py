from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    title: str = Field(max_length=24)
    body: str = Field(max_length=24)
    #date_created:  TIMESTAMP
    author_id: int = Field(ge=1)
    category_id: int = Field(ge=1, default=None)


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)
