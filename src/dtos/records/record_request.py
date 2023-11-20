from pydantic import BaseModel, EmailStr

from src.dtos.records.origin_enum import OriginEnum


class RecordRequest(BaseModel):
    author_name: str
    author_email: EmailStr
    sender_email: EmailStr
    origin: OriginEnum
    success: bool
    content: str
