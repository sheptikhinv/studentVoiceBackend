from typing import List, Annotated

from fastapi import Depends

from . import TokenManager
from ..database import Role, User
from ..exceptions import permissions_exception


class RoleChecker:
    def __init__(self, allowed_roles: List[Role]):
        """
        Initializes the Role Checker object with a list of allowed roles.
        """
        self.allowed_roles = allowed_roles

    def __call__(self, user: Annotated[User, Depends(TokenManager.get_current_user)]):
        """
        Checks if current user has an allowed role.
        """
        if user.role in self.allowed_roles or user.role == Role.ADMIN:
            return True
        raise permissions_exception
