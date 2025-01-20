import fastapi

from models import Todo, Todos
from database import db


app = fastapi.FastAPI()


@app.get("/", response_model=Todos)
def index() -> Todos:

    return Todos(
        todos=db.todos,
    )


@app.post("/todo/")
def create_todo(todo: Todo) -> bool:
    db.add(todo)
    return True
