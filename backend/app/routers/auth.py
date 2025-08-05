from fastapi import APIRouter,HTTPException
from ..models.user import UserOut,UserCreate
from ..repositories.user_repo import (create_user,get_user_by_email)
router=APIRouter()

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