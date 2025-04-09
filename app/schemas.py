from pydantic import BaseModel
from typing import Optional

# 유저 데이터 모델
class UserBase(BaseModel):
    username: str
    email: str

# 유저 생성 시 필요한 데이터 모델
class UserCreate(UserBase):
    password: str

# 유저 정보 반환 시 사용할 모델
class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# 유저 업데이트 시 사용할 모델
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str  # 패스워드는 생성할 때 필요하다.

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8)

class UserCreate(User):
    pass

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=8)] = None

