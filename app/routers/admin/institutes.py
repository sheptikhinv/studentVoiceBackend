from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...database import get_session
from ...schemas import InstituteCreationOutput, InstituteCreationInput
from ...services.institute_service import InstituteService

router = APIRouter(prefix="/insitutes", tags=["Institutes management"])

@router.post("/create", response_model=InstituteCreationOutput)
async def create_institute(institute: InstituteCreationInput, session: AsyncSession = Depends(get_session)):
    return await InstituteService.add_institute(session, institute)


@router.get("/all", response_model=List[InstituteCreationOutput])
async def get_all_institutes(session: AsyncSession = Depends(get_session)):
    return await InstituteService.get_all_institutes(session)