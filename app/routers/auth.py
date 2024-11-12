from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session, User
from ..exceptions import auth_exception
from ..schemas import UserLoginInput, Token, UserViewOutput
from ..helpers import TokenManager, PasswordManager
from ..services import UserService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
async def login(user: UserLoginInput, session: AsyncSession = Depends(get_session)):
    user_db = await UserService.get_user_by_username(session=session, username=user.username)
    if user_db is None or not PasswordManager.verify_password(plain_password=user.password,
                                                              hashed_password=user_db.password):
        raise auth_exception
    return Token(access_token=TokenManager.create_token(data={"sub": str(user_db.id)}), token_type="Bearer")


@router.get("/me", response_model=UserViewOutput)
async def get_me(user: User = Depends(TokenManager.get_current_user), session: AsyncSession = Depends(get_session)):
    return await UserService.get_user_by_id(session=session, user_id=user.id)
