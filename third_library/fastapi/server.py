from fastapi import FastAPI
from uvicorn import run


def create_app():
    app = FastAPI()
    return app
