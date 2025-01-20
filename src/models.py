from pydantic import BaseModel


class Todo(BaseModel):
    text: str
    completed: bool


class Todos(BaseModel):
    todos: list[Todo]