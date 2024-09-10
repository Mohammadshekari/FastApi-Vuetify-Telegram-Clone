from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.hash import Hash
from db.models import DbUser
from routers.schemas import UserBase


def create_user(db: Session, user: UserBase):
    new_user = DbUser(
        fullname=user.fullname,
        phone_number=user.phone_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_phone_number(db: Session, phone_number: str):
    user = db.query(DbUser).filter(DbUser.phone_number == phone_number).first()
    if not user:
        raise HTTPException(
            detail="User with this phone_number does not exist!",
            status_code=404
        )
    return user
