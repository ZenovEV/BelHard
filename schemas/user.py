from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(max_length=24)
    hashed_password: str = Field(max_length=24)
    #is_blocked: Boolen (default=None)
    email: str = Field(max_items=24)


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
