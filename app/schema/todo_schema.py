from pydantic import BaseModel, Field


class TodoResponse(BaseModel):
    id: int
    user_id: int = Field(alias='userId')
    title: str
    completed: bool
