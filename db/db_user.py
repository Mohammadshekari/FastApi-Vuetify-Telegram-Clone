from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.hash import Hash
from db.models import DbUser
from routers.schemas import UserBase


def create_user(db: Session, user: UserBase):
    new_user = DbUser(
        username=user.username,
        phone_number=user.phone_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            detail="User with this username does not exist!",
            status_code=404
        )
    return user
