from pydantic import BaseModel

from ..database import Role


class UserBase(BaseModel):
    username: str


class UserLoginInput(UserBase):
    password: str


class UserCreationInput(UserBase):
    role: Role


class UserCreationOutput(UserCreationInput):
    password: str


class UserViewOutput(UserCreationInput):
    id: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
