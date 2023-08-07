from app.integrations.todo_integration import TodoIntegration
from app.repositories.user_repositories import UserRepositories
from app.schema.todo_schema import TodoResponse
from app.schema.user_schema import UserSchema


class UserService:
    def __init__(self):
        self.user_repository = UserRepositories()
        self.todo_integration = TodoIntegration()

    def get_all_users(self) -> list[UserSchema]:
        return self.user_repository.get_users()

    def get_detail_user_by_id(self, user_id: int) -> UserSchema:
        return self.user_repository.get_detail_user(user_id)

    def get_user_todo_by_user_id(self, user_id: int) -> list[TodoResponse]:
        user = self.user_repository.get_detail_user(user_id)
        if not user:
            return list()

        return self.todo_integration.get_todos(user_id=user_id)

    def ping(self) -> str:
        return "pong"


user_service = UserService()
