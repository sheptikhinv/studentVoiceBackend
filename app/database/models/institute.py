from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Institute(Base):
    __tablename__ = "institutes"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column()
    short_name: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()

    users = relationship("User", back_populates="institute")

    def __repr__(self):
        return f"<Institute {self.id}>"
