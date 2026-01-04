from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
def get_me():
    return {"message": "This is the current user"}


@router.get("/{username}")
def get_user(username: str):
    return {"message": f"User: {username}"}
