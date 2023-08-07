import json
from abc import ABC

import httpx

from app.schema.todo_schema import TodoResponse


class TodoIntegration(ABC):
    def get_todos(self, user_id: int | None) -> list[TodoResponse]:
        url = "https://jsonplaceholder.typicode.com/todos"
        if user_id:
            url += f"?userId={user_id}"

        req = httpx.get(url)
        return req.json()
