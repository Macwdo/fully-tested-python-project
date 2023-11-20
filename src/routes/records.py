from uuid import UUID

from fastapi import APIRouter

from src.dtos.records.record_request import RecordRequest
from src.dtos.records.record_response import RecordResponse

router = APIRouter()


@router.get('/', response_model=list[RecordResponse])
def read_records():
    ...


@router.get('/{uuid}')
def read_record(uuid: UUID, response_model=RecordResponse):
    ...


@router.post('/', response_model=RecordResponse)
def save_record(record_request: RecordRequest):
    return record_request


@router.delete('/{uuid}')
def delete_record(uuid: UUID):
    ...
