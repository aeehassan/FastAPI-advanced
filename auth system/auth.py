from fastapi import APIRouter
from schemas import UserCreate

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup")
def signup(user: UserCreate):
    return {
        "message": "User created",
        "data": user,
    }
