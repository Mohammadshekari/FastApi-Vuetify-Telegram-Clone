import datetime

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.models import DbMessage
from routers.schemas import MessageBase, UserAuth


def create_message(db: Session, message: MessageBase):
    new_message = DbMessage(
        fullname=message.fullname,
        text=message.text,
        created_at=datetime.datetime.now(),
        chat_id=message.chat_id
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


def get_chat_messages(db: Session, chat_id: int):
    return db.query(DbMessage).filter(DbMessage.chat_id == chat_id)


def delete_message(db: Session, pk, username: str):
    message = db.query(DbMessage).filter(DbMessage.id == pk).filter(DbMessage.username == username).first()

    if not message:
        raise HTTPException(
            detail="message not found",
            status_code=404
        )
    db.delete(message)
    db.commit()
    return 'ok'
