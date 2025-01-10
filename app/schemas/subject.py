from pydantic import BaseModel


class SubjectCreationInput(BaseModel):
    name: str


class SubjectCreationOutput(SubjectCreationInput):
    id: int


class SubjectDeletionInput(BaseModel):
    id: int

class SubjectAddProfessorInput(BaseModel):
    professor_id: int
    subject_id: int