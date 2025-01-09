import enum

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Enum as SqlAlchemyEnum, ForeignKey, Column, Integer, Table

from ..database import Base


class Role(enum.Enum):
    PROFESSOR = 1
    ADMIN = 2


subject_professor_association = Table(
    'subject_professor_association', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('professor_id', Integer, ForeignKey('users.id'))
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[Role] = mapped_column(SqlAlchemyEnum(Role), default=Role.PROFESSOR)
    is_active: Mapped[bool] = mapped_column(default=True)

    institute_id: Mapped[int] = mapped_column(ForeignKey("institutes.id"), nullable=True)
    institute = relationship("Institute", back_populates="users")

    subjects = relationship("Subject", secondary=subject_professor_association, back_populates="professors")

    def __repr__(self):
        return f"<User(id='{self.id}')>"
