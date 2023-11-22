from pydantic import BaseModel

from src.dtos.records.record_detail import RecordDetail


class RecordList(BaseModel):
    skip: int
    limit: int
    count: int
    records: list[RecordDetail]
