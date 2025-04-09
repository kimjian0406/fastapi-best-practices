from fastapi import FastAPI
from app.routers import users, auth

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

# Routers
app.include_router(user.router)
from fastapi import FastAPI
from app.routers import user_router, auth_router

app = FastAPI()

# 라우터 포함
app.include_router(user_router.router)
app.include_router(auth_router.router)

# 기본 라우팅
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

