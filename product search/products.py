from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/search")
def get_product(keyword: str, max_results: int = 10):
    return {"search_term": keyword, "limit": max_results}
