from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut

router = APIRouter()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    # TODO: 실제 생성 로직 연결
    return {"id": 1, "email": user.email}

