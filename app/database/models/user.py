import enum

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Enum as SqlAlchemyEnum

from ..database import Base


class Role(enum.Enum):
    PROFESSOR = 1
    ADMIN = 2


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[Role] = mapped_column(SqlAlchemyEnum(Role), default=Role.PROFESSOR)
    is_active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self):
        return f"<User(id='{self.id}')>"
