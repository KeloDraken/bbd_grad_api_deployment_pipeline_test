"""
Pydantic models for the todo list app.
"""

from pydantic import BaseModel


class Todo(BaseModel):
    """
    Pydantic model for a todo item.
    """

    text: str
    completed: bool


class Todos(BaseModel):
    """
    Pydantic model for a list of todo items.
    """

    todos: list[Todo]
