from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
# app/main.py
from fastapi import FastAPI
from app.api import user_api

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(user_api.router)

