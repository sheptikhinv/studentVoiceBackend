from pydantic import BaseModel

from ..database import Role


class UserBase(BaseModel):
    username: str


class UserLogin(UserBase):
    password: str


class UserCreation(UserBase):
    role: Role


class UserCreated(UserCreation):
    password: str


class UserView(UserCreation):
    id: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
