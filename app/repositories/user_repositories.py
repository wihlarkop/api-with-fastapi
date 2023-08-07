from abc import ABC

from app.schema.user_schema import UserSchema


class UserRepositories(ABC):

    def __init__(self):
        self.users: list[UserSchema] = [
            UserSchema(id=1, name="edo"),
            UserSchema(id=2, name="asdf"),
            UserSchema(id=3, name="wp"),
            UserSchema(id=4, name="aw"),
            UserSchema(id=5, name="lol"),
        ]

    def get_users(self) -> list[UserSchema]:
        return self.users

    def get_detail_user(self, user_id: int) -> UserSchema:
        for user in self.users:
            uid = user.get("id")
            if uid == user_id:
                return user
        return UserSchema()
