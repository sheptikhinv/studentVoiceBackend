from fastapi import APIRouter, Depends

from .users import router as users_router
from ...database import Role
from ...helpers import RoleChecker

router = APIRouter(prefix="/admin", dependencies=[Depends(RoleChecker(allowed_roles=[Role.ADMIN]))])

router.include_router(users_router)
