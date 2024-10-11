from datetime import timedelta, datetime

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from helpers import ConfigHelper
from ..database import models, get_session
from ..exceptions import credentials_exception

security = HTTPBearer(auto_error=False)


class TokenManager:
    """
    Everything about authentication
    """
    secret_key = ConfigHelper.get_value("SECRET_KEY")

    @classmethod
    def create_token(cls, data: dict, expires_delta: timedelta | None = None) -> str:
        """
        Creates a JWT token with the given data and expiration delta.
        :param data: Data to encode in JWT.
        :param expires_delta: Timedelta to expire in JWT.
        :return: JWT token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=6)
        to_encode.update({"exp": expire})
        encoded_token = jwt.encode(to_encode, cls.secret_key, algorithm="HS256")
        return encoded_token

    @classmethod
    async def get_current_user(cls, credentials: HTTPAuthorizationCredentials = Depends(security),
                               session=Depends(get_session)) -> models.User:
        """
        Function to get user by given credentials.
        :param credentials: HTTPBearer credentials.
        :param session: Database session.
        :return: User object.
        """
        from . import UserService

        if not credentials:
            raise credentials_exception

        token = credentials.credentials
        try:
            payload = jwt.decode(token, cls.secret_key, algorithms="HS256")
            user_id = payload.get("sub")
            if user_id is None:
                raise credentials_exception
            user = await UserService.get_user_by_id(session=session, user_id=user_id)
            if user is None:
                raise credentials_exception
            return user
        except JWTError as e:
            raise credentials_exception

    @classmethod
    async def optionally_verify_token(cls, credentials: HTTPAuthorizationCredentials = Depends(security,
                                                                                               use_cache=False)) -> models.User | None:
        """
        Function to get user by given credentials.
        :param credentials: HTTPBearer credentials.
        :return: None if token not found, otherwise user object.
        """
        if not credentials:
            return None

        try:
            return await cls.get_current_user(credentials)

        except HTTPException as e:
            return None
