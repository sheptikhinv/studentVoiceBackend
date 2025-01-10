from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import Subject
from app.schemas import SubjectCreationInput


class SubjectService:
    @classmethod
    async def add_subject(cls, subject: SubjectCreationInput, session: AsyncSession) -> Subject:
        subject = Subject(name=subject.name)
        session.add(subject)
        await session.commit()
        return subject

    @classmethod
    async def get_all_subjects(cls, session: AsyncSession) -> list[Subject]:
        result = await session.execute(select(Subject))
        return result.scalars().all()
