from fastapi import APIRouter

from src.modules.todo.todo_schema import TodoIn, TodoUpdate
from src.modules.todo.todo_service import todo_service


class TodoController:
    """
    Todo controller
    """

    def __init__(self):
        self._service = todo_service
        self._prefix = "/todos"
        self.router = APIRouter(prefix=self._prefix)
        self._setup_routes()

    def _setup_routes(self):
        @self.router.get("/")
        async def get_all():
            return await self._service.get_todos()

        @self.router.get("/{todo_id}")
        async def find_on(todo_id: int):
            return await self._service.get_todo_by_id(todo_id=todo_id)

        @self.router.post("/")
        async def create_one(todo: TodoIn):
            return await self._service.create_todo(todo=todo)

        @self.router.put("/{todo_id}")
        async def update_one(todo_id: int, todo: TodoUpdate):
            return await self._service.update_todo(todo_id=todo_id, todo=todo)

        @self.router.delete("/{todo_id}")
        async def delete_one(todo_id: int):
            return await self._service.delete_todo(todo_id=todo_id)


todo_controller = TodoController()
