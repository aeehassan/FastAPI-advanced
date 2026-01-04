from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from typing import Dict

app = FastAPI(title="Dependency Injection")


def get_config():
    return {"env": "production", "version": "1.0.0"}


@app.get("/system-info")
def get_system_info(settings: Dict = Depends(get_config)):
    return settings


@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>Hello world</h1>"


# Dependency that can accept parameters
# If a dependency needs a parameter, it is automatically
# requested for as a query parameter for that endpoint.
#
def pagination_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/items")
def get_items(pager: Dict = Depends(pagination_params)):
    return pager


# Dependency chain
def get_token(token: str):
    return token


def get_user(token: str = Depends(get_token)):
    return {"username": "admin", "token_used": token}


@app.get("/users/me")
def get_current_user(user: Dict = Depends(get_user)):
    return user
