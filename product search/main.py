from fastapi import FastAPI
from products import router as products_route

app = FastAPI(title="Product search")
app.include_router(products_route)


@app.get("/")
def root():
    return "Hello wworld!"
