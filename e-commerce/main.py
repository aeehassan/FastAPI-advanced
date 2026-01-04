from routes.customers_route import router as customers_route
from routes.inventory_route import router as inventory_route
from fastapi import FastAPI

app = FastAPI(title="Ecommerce API")
app.include_router(customers_route)
app.include_router(inventory_route)


@app.get("/")
def root():
    return "Hello world"
