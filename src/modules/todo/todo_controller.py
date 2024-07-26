from fastapi import APIRouter

from src.modules.todo.todo_service import todo_service


class TodoController:
    """
    Todo controller
    """

    def __init__(self):
        self.service = todo_service
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        @self.router.get("/")
        async def get_app_info(todo_id: int):
            """Root endpoint"""
            return await self.service.get_todo_by_id(todo_id=todo_id)


todo_controller = TodoController()
