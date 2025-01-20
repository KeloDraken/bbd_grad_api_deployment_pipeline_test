"""
Database module
"""

from src.models import Todo


class DB:
    """
    Database class
    """

    def __init__(self):
        self.todos: list[Todo] = [
            Todo(text="TODO 1", completed=False),
            Todo(text="TODO 2", completed=True),
            Todo(text="TODO 3", completed=True),
            Todo(text="TODO 4", completed=False),
        ]

    def add(self, todo: Todo) -> None:
        """
        Add a todo to the database
        """
        self.todos.append(todo)


db = DB()
