from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user

router = APIRouter()

@router.post("/users", response_model=UserOut)
def register_user(user: UserCreate):
    return create_user(user)

