from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app import Subject, User
from app.database.models.user import subject_professor_association
from app.schemas import SubjectCreationInput, SubjectAddProfessorInput, SubjectGetByIdInput


class SubjectService:
    @classmethod
    async def add_subject(cls, subject_schema: SubjectCreationInput, session: AsyncSession) -> Subject:
        subject = Subject(name=subject_schema.name)
        session.add(subject)
        await session.commit()
        return subject

    @classmethod
    async def get_all_subjects(cls, session: AsyncSession) -> list[Subject]:
        result = await session.execute(select(Subject))
        return result.scalars().all()

    @classmethod
    async def add_professor_to_subject(cls, schema: SubjectAddProfessorInput, session: AsyncSession) -> Subject:
        subject = await session.get(Subject, schema.subject_id)
        professor = await session.get(User, schema.professor_id)

        if not subject or not professor:
            raise ValueError('Subject or professor must be provided')

        await session.execute(
            insert(subject_professor_association).values(subject_id=subject.id, professor_id=professor.id))
        await session.commit()
        return await cls.get_subject_by_id(subject.id, session)

    @classmethod
    async def get_subject_by_id(cls, subject_id: int, session: AsyncSession) -> Subject:
        result = await session.execute(
            select(Subject).where(subject_id == Subject.id).options(selectinload(Subject.professors)))
        return result.scalar_one_or_none()
