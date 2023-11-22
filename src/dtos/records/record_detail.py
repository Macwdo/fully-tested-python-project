from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class RecordDetail(BaseModel):
    id: UUID
    sender_id: int
    sender_email: str
    receiver_email: str
    success: bool
    content: str
    created_at: datetime
    updated_at: datetime
