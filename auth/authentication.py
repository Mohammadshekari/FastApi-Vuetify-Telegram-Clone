import random
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Body, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from auth.oauth2 import create_access_token
from db.database import get_db
from db.db_user import create_user
from db.hash import Hash
from db.models import DbUser
from routers.schemas import UserBase

router = APIRouter(
    tags=['authentication'],
    prefix="/api/v1/auth"
)

user_tokens = {}


def send_sms(phone_number: str) -> None:
    token = random.randint(10000, 99999)
    user_tokens[phone_number] = token
    print('Sending SMS to', phone_number, " Token:", token)


class LoginUser(BaseModel):
    phone_number: str
    code: Optional[int] = None


@router.post('/login')
def login(request: LoginUser, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.phone_number == request.phone_number).first()
    if not request.code:
        send_sms(request.phone_number)
        return {
            'ok': True,
            'message': "Token sent."
        }
    phone_number_token = user_tokens.get(request.phone_number)
    if not phone_number_token or phone_number_token != request.code:
        return {
            'ok': False,
            'message': "Invalid Code!"
        }

    if not user:
        user = create_user(db, UserBase(
            fullname="telegram user",
            phone_number=request.phone_number
        ))
    access_token = create_access_token(data={
        'phone_number': user.phone_number,
    })

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'phone_number': user.phone_number,
    }
