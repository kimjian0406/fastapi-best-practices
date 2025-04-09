from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

# 유저 데이터 모델
class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    age: int

# 유저 데이터 저장소 (간단한 메모리 저장소)
fake_users_db = {}

app = FastAPI()

# 유저 생성 엔드포인트
@app.post("/users/", response_model=User)
async def create_user(user: User):
    user.id = str(uuid4())  # 고유 ID 생성
    fake_users_db[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = fake_users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@app.get("/users", response_model=List[User])
async def get_users():
    return list(fake_users_db.values())

from fastapi import HTTPException

# 유저 업데이트 엔드포인트
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    fake_users_db[user_id] = user
    return user
@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = fake_users_db.pop(user_id)
    return deleted_user

@app.get("/users", response_model=List[User])
async def get_users():
    return list(fake_users_db.values())

