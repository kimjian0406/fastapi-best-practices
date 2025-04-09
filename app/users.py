from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UserUpdate
from .auth import get_current_user
from .models import User as DBUser

router = APIRouter()

@router.get("/me", response_model=User)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=User)
async def update_profile(user_update: UserUpdate, current_user: User = Depends(get_current_user)):
    db_user = DBUser.objects(username=current_user.username).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user_update.email:
        db_user.email = user_update.email
    if user_update.password:
        db_user.password = user_update.password
    db_user.save()
    return db_user

