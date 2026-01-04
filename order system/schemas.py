from pydantic import BaseModel


class OrderUpdate(BaseModel):
    new_address: str
