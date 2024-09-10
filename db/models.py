from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Table

chat_users = Table(
    'chat_users',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('chat_id', Integer, ForeignKey('chats.id'), primary_key=True)
)


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    phone_number = Column(String, unique=True)
    created_at = Column(DateTime)
    # password = Column(String)
    chats = relationship('DbChat', secondary=chat_users, back_populates='users')


class DbChat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    file_url = Column(String)
    file_type = Column(String)
    text = Column(Text(1000))
    created_at = Column(DateTime)
    is_group = Column(Boolean)
    users = relationship('DbUser', secondary=chat_users, back_populates='chats')
    messages = relationship('DbMessage', back_populates='chat')


class DbMessage(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    username = Column(String)
    created_at = Column(DateTime)
    chat_id = Column(Integer, ForeignKey('chats.id'))
    chat = relationship('DbChat', back_populates='messages')
