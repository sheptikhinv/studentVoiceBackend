from pydantic import BaseModel

from .user import UserViewOutput


class InstituteBase(BaseModel):
    full_name: str
    short_name: str
    address: str


class InstituteCreationInput(InstituteBase):
    ...


class InstituteCreationOutput(InstituteBase):
    id: int


class InstituteViewOutput(InstituteCreationOutput):
    users: list[UserViewOutput]
