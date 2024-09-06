import random

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.oauth2 import create_access_token
from db.database import get_db
from db.hash import Hash
from db.models import DbUser

router = APIRouter(
    tags=['authentication']
)

user_tokens = {}


def send_sms(phone_number: str) -> None:
    token = random.randint(10000, 99999)
    user_tokens[phone_number] = token
    print('Sending SMS to', phone_number, " Token:", token)


@router.post('/login')
def login(phone_number: str, code: int = None, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.phone_number == phone_number).first()
    if not user:
        raise HTTPException(detail="There is no user with this credential!", status_code=404)
    if not code:
        send_sms(phone_number)
        return {
            'ok': True,
            'message': "Token sent."
        }
    phone_number_token = user_tokens.get(phone_number)
    if not phone_number_token or phone_number_token != code:
        return {
            'ok': False,
            'message': "Invalid Code!"
        }

    access_token = create_access_token(data={
        'phone_number': user.phone_number,
    })

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'phone_number': user.phone_number,
    }
