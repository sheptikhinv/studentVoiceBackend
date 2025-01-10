from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import Subject
from app.database import get_session
from app.schemas import SubjectCreationInput, SubjectCreationOutput, SubjectGetByIdOutput, SubjectAddProfessorInput, \
    SubjectGetByIdInput
from app.services import SubjectService

router = APIRouter(prefix="/subjects", tags=["Subjects management"])


@router.post("/add", response_model=SubjectCreationOutput)
async def create_subject(subject: SubjectCreationInput, session: AsyncSession = Depends(get_session)):
    return await SubjectService.add_subject(subject, session)


@router.post("/attach_professor", response_model=SubjectGetByIdOutput)
async def add_professor(schema: SubjectAddProfessorInput, session: AsyncSession = Depends(get_session)):
    return await SubjectService.add_professor_to_subject(schema, session)


@router.get("/{subject_id}", response_model=SubjectGetByIdOutput)
async def get_subject(subject_id: int, session: AsyncSession = Depends(get_session)):
    return await SubjectService.get_subject_by_id(subject_id, session)
