from fastapi.routing import APIRoute

from app.controller.user_controller import get_all_users, get_detail_user, get_user_todo

routes = [
    APIRoute('/users/', endpoint=get_all_users, methods=['GET'], tags=['Users']),
    APIRoute('/users/{user_id}', endpoint=get_detail_user, methods=['GET'], tags=['Users']),
    APIRoute('/users/{user_id}/todos', endpoint=get_user_todo, methods=['GET'], tags=['Users']),
]
