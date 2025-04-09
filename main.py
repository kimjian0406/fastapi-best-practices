from fastapi import FastAPI
from app.api import user

app = FastAPI()

app.include_router(user.router)

from fastapi import FastAPI
from app.api import users

app = FastAPI()

app.include_router(users.router)

