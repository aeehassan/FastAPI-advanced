from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/list")
def get_list():
    return {"message": "List of items"}


@router.get("/details")
def get_details():
    return {"message": "Item details"}
