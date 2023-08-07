from app.schema.todo_schema import TodoResponse
from app.schema.user_schema import UserSchema
from app.services.user_service import UserService
from fastapi import Request, Depends, APIRouter


async def get_all_users(
        request: Request,
        user: UserService = Depends()
) -> list[UserSchema]:
    return user.get_all_users()


async def get_detail_user(
        request: Request,
        user_id: int,
        user: UserService = Depends()
) -> UserSchema:
    return user.get_detail_user_by_id(user_id)


async def get_user_todo(
        request: Request,
        user_id: int,
        user: UserService = Depends()
) -> list[TodoResponse]:
    todos = user.get_user_todo_by_user_id(user_id)
    return todos
