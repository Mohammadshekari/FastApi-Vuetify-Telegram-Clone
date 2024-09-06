import datetime
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    fullname: str
    phone_number: str


class UserDisplay(BaseModel):
    fullname: str
    phone_number: str


class ChatUser(BaseModel):
    fullname: str


class ChatMessage(BaseModel):
    text: str
    fullname: str
    created_at: datetime.datetime


class ChatBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class ChatDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    created_at: datetime.datetime
    user: ChatUser
    comments: List[ChatMessage]


class MessageDisplay(BaseModel):
    fullname: str
    text: str


class UserAuth(BaseModel):
    id: int
    fullname: str
    phone_number: str


class MessageBase(BaseModel):
    fullname: str
    text: str
    post_id: int
