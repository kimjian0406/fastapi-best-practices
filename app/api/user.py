# app/api/user_api.py
from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from app.services.user_service import create_user

router = APIRouter()

@router.post("/users", response_model=User)
def create_user_view(user: UserCreate):
    return create_user(user)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.servicesuserservice import create_user, authenticate_user, login_user
from app.user_schema import UserCreate, UserOut

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user_create: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_create)
    return user

@router.post("/login")
def login(user_create: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_create.email, user_create.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return login_user(user)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_schema import UserCreate, UserOut
from app.services.userservice import create_user, get_user_by_email

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

