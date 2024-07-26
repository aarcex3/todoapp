"""Todo Service

"""

from datetime import datetime

from fastapi import HTTPException, Response, status
from sqlmodel import Session, select

from src.database import DB, Database
from src.modules.todo.todo_model import Todo
from src.modules.todo.todo_schema import TodoIn, TodoOut, TodoUpdate


class TodoService:
    """Todo Service"""

    def __init__(self, db: Database):
        self.service_name: str = "Todo Service"
        self.db: Session = db.get_session()

    async def get_todo_by_id(self, todo_id: int):
        """Get one todo by its id

        Args:
            todo_id (int): The id of the todo to retrieve

        Returns:
            Todo: A dictinary representing the found todo
        """ """ """
        return self.db.exec(select(Todo).where(Todo.id == todo_id)).one()

    async def get_todos(self):
        """Get all the todos in the DB

        Returns:
            list[Todo]: A list of todos
        """
        return self.db.exec(select(Todo)).all()

    async def create_todo(self, todo: TodoIn):
        """Create on todo

        Args:
            todo (TodoIn): The todo schema
        """
        new_todo = Todo(title=todo.title, description=todo.description)
        try:
            self.db.add(new_todo)
            self.db.commit()
            self.db.refresh(new_todo)
            return TodoOut(**new_todo.model_dump())
        except Exception as ex:
            raise HTTPException(
                detail=ex,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ) from ex

    async def update_todo(self, todo_id: int, todo: TodoUpdate):
        """Update one todo

        Args:
            todo_id (int): The id of the todo
            todo (TodoUpdate): The data to update the todo

        Raises:
            HTTPException: If something failes

        Returns:
            TodoOut: The updated todo
        """
        updated_todo = self.db.exec(select(Todo).where(Todo.id == todo_id)).one()

        updated_todo.title = todo.title if todo.title else updated_todo.title
        updated_todo.description = (
            todo.description if todo.description else updated_todo.description
        )
        updated_todo.is_complete = (
            todo.is_complete if todo.is_complete else updated_todo.is_complete
        )
        updated_todo.updated_at = datetime.now()

        self.db.add(updated_todo)
        try:
            self.db.commit()
            self.db.refresh(updated_todo)
            return TodoOut(**updated_todo)
        except Exception as ex:
            raise HTTPException(
                detail=ex,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ) from ex

    async def delete_todo(self, todo_id: int):
        """Delete todo by id

        Args:
            todo_id (int): The id of the todo

        Raises:
            HTTPException: If something failes
        """
        todo = self.db.exec(select(Todo).where(Todo.id == todo_id)).one()
        try:
            self.db.delete(todo)
            self.db.commit()
            return Response(content="Todo deleted!", status_code=status.HTTP_200_OK)
        except Exception as ex:
            raise HTTPException(
                detail=ex,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ) from ex


todo_service = TodoService(db=DB)
