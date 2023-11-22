from pydantic import BaseModel, EmailStr


class RecordRequest(BaseModel):
    sender_id: int
    sender_email: EmailStr
    receiver_email: EmailStr
    success: bool
    content: str
