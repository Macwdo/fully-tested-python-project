from pydantic import BaseModel


class BaseResponse(BaseModel):
    message: str
    success: bool
    status_code: int
