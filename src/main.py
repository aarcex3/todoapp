import uvicorn
from fastapi import FastAPI

from src.app_module import app_module

app = FastAPI()

app.include_router(app_module.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
