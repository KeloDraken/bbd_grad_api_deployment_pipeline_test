"""
Main module.
"""

import fastapi

from src.models import Todo, Todos
from src.database import db


app = fastapi.FastAPI()


@app.get("/", response_model=Todos)
def index() -> Todos:
    """
    Get all todos.
    """
    return Todos(
        todos=db.todos,
    )


@app.post("/todo/")
def create_todo(todo: Todo) -> bool:
    """
    Create a new todo.
    """
    db.add(todo)
    return True
