from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr

from src.dtos.records.origin_enum import OriginEnum


class RecordResponse(BaseModel):
    record_id: UUID
    author_name: str
    author_email: EmailStr
    sender_email: EmailStr
    origin: OriginEnum
    success: bool
    content: str
    created_at: datetime
    updated_at: datetime
