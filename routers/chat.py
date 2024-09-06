import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from starlette import status

from auth.oauth2 import get_current_user
from db.database import get_db
from db.db_chat import create_chat, get_all_chats, delete_chat
from routers.schemas import ChatDisplay, ChatBase, UserAuth

router = APIRouter(
    tags=['chat'],
    prefix="/chat"
)

image_url_types = ['absolute', 'relative']


@router.post('/', response_model=ChatDisplay)
def create_chat_api(
        request_chat: ChatBase,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(get_current_user)
):
    if request_chat.image_url_type not in image_url_types:
        raise HTTPException(
            detail="Invalid url type! should be 'absolute' or 'relative'.",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    request_chat.creator_id = current_user.id
    return create_chat(db, request_chat)


@router.get('/all', response_model=List[ChatDisplay])
def get_all_chats_api(db: Session = Depends(get_db)):
    return get_all_chats(db)


@router.delete('/{pk}', )
def chat_delete_api(
        pk: int,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(get_current_user)
):
    return delete_chat(db, pk, current_user.id)


@router.post('/image', )
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    strings = string.ascii_letters
    rand_str = ''.join(random.choice(strings) for i in range(6))
    name = f'_{rand_str}.'
    path = 'media/' + name.join(image.filename.rsplit('.', 1))
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {
        'filename': path
    }
