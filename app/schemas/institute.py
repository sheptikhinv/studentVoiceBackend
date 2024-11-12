from pydantic import BaseModel


class InstituteBase(BaseModel):
    full_name: str
    short_name: str
    address: str


class InstituteCreationInput(InstituteBase):
    ...


class InstituteCreationOutput(InstituteBase):
    id: int
