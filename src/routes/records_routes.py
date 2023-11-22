from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.utils import get_session
from src.dtos.records.record_detail import RecordDetail
from src.dtos.records.record_list import RecordList
from src.dtos.records.record_request import RecordRequest
from src.models.record import Record

router = APIRouter()


@router.get('/', response_model=RecordList)
def read_records(
    q: str = '',
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    if q:
        records = session.scalars(
            select(Record)
            .filter(
                (Record.content.icontains(q))
                | (Record.receiver_email.icontains(q))
                | (Record.sender_email.icontains(q))
            )
            .offset(skip)
            .limit(limit)
        ).all()
    else:
        records = session.scalars(
            select(Record).offset(skip).limit(limit)
        ).all()

    return {
        'count': len(records),
        'skip': skip,
        'limit': limit,
        'records': records,
    }


@router.get('/{id}', response_model=RecordDetail)
def read_record(id: UUID, session: Session = Depends(get_session)):
    record = session.scalar(select(Record).where(Record.id == id))
    if record:
        return RecordDetail.model_validate(record)
    raise HTTPException(
        status.HTTP_404_NOT_FOUND, f'Record by id {id} not found'
    )


@router.post('/', response_model=RecordDetail)
def save_record(
    record_request: RecordRequest, session: Session = Depends(get_session)
):
    record_model = Record(
        **record_request.model_dump(),
    )
    session.add(record_model)
    session.commit()

    return record_model


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_record(id: UUID, session: Session = Depends(get_session)):
    record = session.scalar(select(Record).where(Record.id == id))
    if record:
        session.delete(record)
        session.commit()
        return {'message': f'record by id {id} was deleted'}
    raise HTTPException(
        status.HTTP_404_NOT_FOUND, f'Record by id {id} not found'
    )
