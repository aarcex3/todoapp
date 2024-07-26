class TodoService:
    """Todo Service"""

    def __init__(self):
        self.service_name = "Todo App"

    async def get_todo_by_id(self, todo_id: int):
        return {"id": todo_id}


todo_service = TodoService()
