from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class Record(Base):
    __tablename__ = 'records'

    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int]
    sender_email: Mapped[str]
    receiver_email: Mapped[str]
    success: Mapped[bool]
    content: Mapped[str]
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self) -> str:
        return f'Record(id={str(self.id)[:6]}..., sender_email={self.sender_email})'

    def str(self) -> str:
        return f'Record(id={str(self.id)[:6]}..., sender_email={self.sender_email})'
