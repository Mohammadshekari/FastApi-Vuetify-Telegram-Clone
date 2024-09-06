from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.db_user import create_user
from routers.schemas import UserDisplay, UserBase

router = APIRouter(
    tags=['user'],
    prefix="/user"
)


@router.post('/', response_model=UserDisplay)
def create_user_api(request_user: UserBase, db: Session = Depends(get_db)):
    return create_user(db, request_user)
