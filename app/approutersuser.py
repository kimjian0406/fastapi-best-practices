from fastapi import APIRouter, Depends, HTTPException
from app.schemas import User, UserCreate
from app.services.user import UserService
from sqlalchemy.orm import Session
from app.database import get_db  # DB 연결 함수

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)

@router.get("/users/", response_model=List[User])
async def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return UserService.get_user(user_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.update_user(user_id, user, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return UserService.delete_user(user_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

