from __future__ import absolute_import

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class RecordResponse(BaseModel):
    id: UUID
    sender_id: int
    sender_email: str
    receiver_email: str
    success: bool
    content: str
    created_at: datetime
    updated_at: datetime


class ListResponse(BaseModel):
    size: int | None
    skip: int
    limit: int


class RecordListResponse(ListResponse):
    records: list[RecordResponse]


class RecordRequest(BaseModel):
    sender_id: int
    sender_email: EmailStr
    receiver_email: EmailStr
    success: bool
    content: str
