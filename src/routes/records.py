from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.utils import get_session
from src.models.record import Record
from src.schemas.records import (
    RecordListResponse,
    RecordRequest,
    RecordResponse,
)

router = APIRouter()


@router.get('/', response_model=RecordListResponse)
def read_records(
    q: str = '',
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
) -> RecordListResponse:
    if q:
        records = session.scalars(
            select(Record).filter(
                (Record.content.icontains(q))
                | (Record.receiver_email.icontains(q))
                | (Record.sender_email.icontains(q))
            )
        ).all()
    else:
        records = session.scalars(
            select(Record).offset(skip).limit(limit)
        ).all()

    records_response = [
        RecordResponse(**record.__dict__) for record in records
    ]

    return RecordListResponse(
        size=len(records_response),
        skip=skip,
        limit=limit,
        records=records_response,
    )


@router.get('/{id}', response_model=RecordResponse)
def read_record(id: int, session: Session = Depends(get_session)) -> Record:
    record = session.scalar(select(Record).where(Record.id == id))
    if record:
        return record
    raise HTTPException(
        status.HTTP_404_NOT_FOUND, f'Record by id {id} not found'
    )


@router.post(
    '/', response_model=RecordResponse, status_code=status.HTTP_201_CREATED
)
def save_record(
    record_request: RecordRequest, session: Session = Depends(get_session)
) -> Record:
    record_model = Record(
        **record_request.model_dump(),
    )
    session.add(record_model)
    session.commit()

    return record_model


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_record(id: int, session: Session = Depends(get_session)) -> None:
    record = session.scalar(select(Record).where(Record.id == id))
    if record:
        session.delete(record)
        session.commit()
        return

    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
    )
