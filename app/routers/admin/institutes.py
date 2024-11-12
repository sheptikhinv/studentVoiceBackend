from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...database import get_session
from ...schemas import InstituteCreationOutput, InstituteCreationInput, InstituteViewOutput
from ...services.institute_service import InstituteService

router = APIRouter(prefix="/insitutes", tags=["Institutes management"])


@router.post("/create", response_model=InstituteCreationOutput)
async def create_institute(institute: InstituteCreationInput, session: AsyncSession = Depends(get_session)):
    return await InstituteService.add_institute(session, institute)


@router.get("/{instute_id}", response_model=InstituteViewOutput)
async def get_institute_by_id(institute_id: int, session: AsyncSession = Depends(get_session)):
    return await InstituteService.get_institute_by_id(session, institute_id)


@router.get("/all", response_model=List[InstituteCreationOutput])
async def get_all_institutes(session: AsyncSession = Depends(get_session)):
    return await InstituteService.get_all_institutes(session)
