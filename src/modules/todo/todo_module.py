from fastapi import APIRouter

from src.modules.todo.todo_controller import todo_controller


class TodoModule:
    """'Todo Module"""

    def __init__(self):
        self.router = APIRouter()
        self.router.include_router(todo_controller.router, tags=["Todo"])


todo_module = TodoModule()
