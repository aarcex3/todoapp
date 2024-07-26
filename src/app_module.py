from fastapi import APIRouter

from src.app_controller import app_controller
from src.modules.todo.todo_module import todo_module


class AppModule:
    """'App Module"""

    def __init__(self):
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        self.router.include_router(app_controller.router, prefix="/app", tags=["app"])
        self.router.include_router(todo_module.router)


app_module = AppModule()
