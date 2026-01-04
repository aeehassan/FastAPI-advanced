from fastapi import FastAPI
from auth import router as auth_route

app = FastAPI(title="Auth System")
app.include_router(auth_route)


@app.get("/")
def root():
    return "Hello world"
