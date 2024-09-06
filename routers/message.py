import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from starlette import status

from auth.oauth2 import get_current_user
from db.database import get_db
from db.db_message import create_message, get_chat_messages, delete_message
from routers.schemas import MessageDisplay, MessageBase, UserAuth

router = APIRouter(
    tags=['message'],
    prefix="/message"
)

image_url_types = ['absolute', 'relative']


@router.post('/', response_model=MessageDisplay)
def create_message_api(
        request_message: MessageBase,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(get_current_user)
):
    # request_message.fullname = current_user.fullname
    return create_message(db, request_message)


@router.get('/all/{chat_id}', response_model=List[MessageDisplay])
def get_all_messages_api(chat_id: int, db: Session = Depends(get_db)):
    return get_chat_messages(db, chat_id)


@router.delete('/{pk}', )
def message_delete_api(
        pk: int,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(get_current_user)
):
    return delete_message(db, pk, current_user.username)
