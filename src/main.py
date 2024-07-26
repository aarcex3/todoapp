import uvicorn
from fastapi import FastAPI

from src.app_module import app_module
from src.database import DB

app = FastAPI()

app.include_router(app_module.router, prefix="/api/v1")


if __name__ == "__main__":
    DB.create_db_and_tables()
    uvicorn.run(app, host="0.0.0.0", port=8000)
