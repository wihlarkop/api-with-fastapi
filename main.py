import uvicorn
from fastapi import FastAPI

from app.controller.user_controller import router
from app.router import routes

app = FastAPI(routes=routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router, prefix="/users", tags=["data"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
