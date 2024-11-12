from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import Institute
from ..schemas import InstituteCreationInput, InstituteCreationOutput


class InstituteService:
    @classmethod
    async def add_institute(cls, session: AsyncSession, institute: InstituteCreationInput) -> InstituteCreationOutput:
        new_institute = Institute(full_name=institute.full_name, short_name=institute.short_name,
                                  address=institute.address)
        session.add(new_institute)
        await session.commit()
        return InstituteCreationOutput(id=new_institute.id, full_name=institute.full_name,
                                       short_name=institute.short_name, address=institute.address)

    @classmethod
    async def get_institute_by_id(cls, session: AsyncSession, institute_id: int) -> Institute | None:
        result = await session.execute(select(Institute).where(Institute.id == institute_id))
        return result.scalar_one_or_none()

    @classmethod
    async def get_all_institutes(cls, session: AsyncSession) -> List[Institute]:
        result = await session.execute(select(Institute))
        return result.scalars().all()
