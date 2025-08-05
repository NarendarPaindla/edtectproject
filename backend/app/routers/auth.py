from fastapi import APIRouter,HTTPException,Response
from itsdangerous import TimestampSigner
from ..config import settings
from ..models.user import UserOut,UserCreate,UserLogin
from ..repositories.user_repo import (create_user,get_user_by_email,authenticate_user)
router=APIRouter()
signer=TimestampSigner(settings.SECRET_KEY)
SESSION_COOKIE="edtech_session"
@router.post("/register",response_model=UserOut)
async def register(user: UserCreate):
    if await get_user_by_email(user.email):
        raise HTTPException(400,"Email already registered")
    created=await create_user(user)
    return UserOut(
        id=str(created["_id"]),
        email=created["email"],
        role=created["role"],
        name=created["name"]
    )

@router.post("/login")
async def login(user: UserLogin, response: Response):
    db_user = await authenticate_user(user.email, user.password)
    if not db_user:
        raise HTTPException(400, "Invalid credentials")
    # Sign and set session cookie
    token = signer.sign(str(db_user["_id"]).encode()).decode()
    response.set_cookie(
        key=SESSION_COOKIE,
        value=token,
        httponly=True,
        max_age=7*24*3600,  # 1 week
        samesite="lax"
    )
    return {"message": "Logged in successfully"}
