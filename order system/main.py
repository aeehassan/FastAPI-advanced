from fastapi import FastAPI
from orders import router as orders_route

app = FastAPI(title="Order System")
app.include_router(orders_route)


@app.get("/")
def root():
    return "Hello world!!"
