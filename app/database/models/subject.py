from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .user import subject_professor_association


class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    professors = relationship("User", secondary=subject_professor_association, back_populates="subjects")
