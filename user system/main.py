from fastapi import FastAPI
from users import router as user_route

app = FastAPI(title="User system")
app.include_router(user_route)


@app.get("/")
def root():
    return "Hello world"
