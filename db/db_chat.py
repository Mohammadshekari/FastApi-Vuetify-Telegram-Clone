import datetime

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.models import DbChat
from routers.schemas import ChatBase, UserAuth


def create_chat(db: Session, chat: ChatBase):
    new_chat = DbChat(
        image_url=chat.image_url,
        image_url_type=chat.image_url_type,
        caption=chat.caption,
        timestamp=datetime.datetime.now(),
        user_id=chat.creator_id,
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat


def get_all_chats(db: Session):
    return db.query(DbChat).all()


def delete_chat(db: Session, pk, user_id: int):
    chat = db.query(DbChat).filter(DbChat.id == pk).filter(DbChat.user_id == user_id).first()

    if not chat:
        raise HTTPException(
            detail="chat not found",
            status_code=404
        )
    db.delete(chat)
    db.commit()
    return 'ok'
