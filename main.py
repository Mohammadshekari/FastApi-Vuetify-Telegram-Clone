import datetime
import os
from enum import Enum

from starlette.middleware.cors import CORSMiddleware

from db import models
from db.database import engine
from routers import user, chat, message
from auth import authentication

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Body, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

load_dotenv('.env')
SECRET_KEY = os.getenv('SECRET_KEY')

app = FastAPI()
app.include_router(authentication.router)
app.include_router(message.router)
app.include_router(user.router)
app.include_router(chat.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(engine)

origins = [host for host in os.getenv('ALLOWED_CORS', '').split(',')]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

app.mount('/media', StaticFiles(directory='media'), name='media')


@app.get("/")
async def index_view(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login_to_app")
async def index_views(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
