from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from .institute_service import InstituteService
from ..database import Role
from ..helpers import PasswordManager
from ..database.models import User
from ..exceptions import username_already_taken_exception, professor_without_institute_exception
from ..schemas import UserCreationInput, UserCreationOutput


class UserService:
    @classmethod
    async def add_user(cls, session: AsyncSession, user: UserCreationInput) -> UserCreationOutput:
        if await cls.get_user_by_username(session, user.username) is not None:
            raise username_already_taken_exception

        if user.role == Role.PROFESSOR and user.institute_id is None or await InstituteService.get_institute_by_id(
                session, user.institute_id) is None:
            raise professor_without_institute_exception

        password = PasswordManager.get_random_password()
        new_user = User(username=user.username, password=PasswordManager.get_password_hash(password),
                        role=user.role, institute_id=user.institute_id)
        session.add(new_user)
        await session.commit()
        return UserCreationOutput(username=user.username, password=password, role=user.role, id=new_user.id,
                                  institute_id=user.institute_id)

    @classmethod
    async def get_user_by_id(cls, session: AsyncSession, user_id: int) -> User | None:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    @classmethod
    async def get_user_by_username(cls, session: AsyncSession, username: str) -> User | None:
        result = await session.execute(select(User).where(func.lower(User.username) == username.lower()))
        return result.scalar_one_or_none()

    @classmethod
    async def get_all_users(cls, session: AsyncSession) -> list[User]:
        result = await session.execute(select(User))
        return result.scalars().all()
