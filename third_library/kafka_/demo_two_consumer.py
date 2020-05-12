import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="SpiderKeeper",
    version="2.0",
)

api = APIRouter()


@api.get('/')
def index(
        offset: int = None
):
    return {}


app.include_router(api)

if __name__ == '__main__':
    uvicorn.run('third_library.kafka_.demo_two_consumer:app')
