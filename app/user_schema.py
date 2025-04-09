# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
from pydantic import BaseModel, EmailStr

# 유저 생성 요청용
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# 유저 응답용
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # Pydantic v2에서 orm_mode 대체

