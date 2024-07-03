from typing import TYPE_CHECKING
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .tasks import Task


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    tasks: list["Task"] = Relationship(back_populates="owner")


class UserPublic(UserBase):
    id: int


class UserRegister(UserBase):
    password: str = Field(min_length=8, max_length=40)

class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(SQLModel):
    sub: int | None = None