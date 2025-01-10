from pydantic import BaseModel

from app.schemas import UserViewOutput


class SubjectCreationInput(BaseModel):
    name: str


class SubjectCreationOutput(SubjectCreationInput):
    id: int


class SubjectDeletionInput(BaseModel):
    id: int


class SubjectAddProfessorInput(BaseModel):
    professor_id: int
    subject_id: int


class SubjectGetByIdInput(BaseModel):
    id: int


class SubjectGetByIdOutput(SubjectGetByIdInput):
    name: str
    professors: list[UserViewOutput]
