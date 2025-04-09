from app.schemas.user import UserCreate, UserOut

def create_user(user_data: UserCreate) -> UserOut:
    # 예시용 가짜 유저 생성
    return UserOut(id=1, email=user_data.email, username=user_data.username)

