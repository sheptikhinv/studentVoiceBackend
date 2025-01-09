from datetime import datetime, UTC

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, validates

from ..database import Base


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    reviewer_name: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    # class
    grade: Mapped[int] = mapped_column()

    @validates('grade')
    def validate_grade(self, key, value):
        if not 1 <= value <= 5:
            raise ValueError(f'Grade must be between 1 and 5')
        return value
