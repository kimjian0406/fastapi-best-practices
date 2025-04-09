# app/api/user_api.py
from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from app.services.user_service import create_user

router = APIRouter()

@router.post("/users", response_model=User)
def create_user_view(user: UserCreate):
    return create_user(user)

