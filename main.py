import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.controller.user_controller import router
from app.router import routes

app = FastAPI(routes=routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=settings.DEBUG)
