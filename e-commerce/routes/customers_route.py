from fastapi import APIRouter

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/profile")
def get_profile():
    return {"message": "Customer profile"}


@router.post("/login")
def login():
    return {"message": "Customer logged in"}
