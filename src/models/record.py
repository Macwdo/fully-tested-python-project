from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.dtos.records.origin_enum import OriginEnum


class Record(Base):
    __tablename__ = 'records'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    author_name: Mapped[str]
    author_email: Mapped[str]
    sender_email: Mapped[str]
    origin: Mapped[OriginEnum]
    success: Mapped[bool]
    content: Mapped[str]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    def __repr__(self) -> str:
        return (
            f'Record(id={str(self.id)[:6]}..., author_name={self.author_name})'
        )

    def str(self) -> str:
        return (
            f'Record(id={str(self.id)[:6]}..., author_name={self.author_name})'
        )
