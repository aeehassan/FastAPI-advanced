from fastapi import APIRouter
from schemas import OrderUpdate

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/{order_id}/update")
def make_order(
    order_id: int,
    update_data: OrderUpdate,
    express_delivery: bool = False,
):
    return {
        "id": order_id,
        "address": update_data.new_address,
        "express": express_delivery,
    }
