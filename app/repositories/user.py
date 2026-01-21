from typing import Protocol, Union
from dishka import make_async_container, Provider, provide, Scope

class UserRepo(Protocol):
    def by_id(self, id: str) -> dict[str, str] | None:
        ...

class UserRepoLocal(UserRepo):
    def __init__(self):
        self.user_map = [
            {
                "id": "1",
                "name": "First User"
            },
            {
                "id": "2",
                "name": "Second User"
            },
            {
                "id": "3",
                "name": "Third User"
            }
        ]

    def by_id(self, id: str) -> dict[str, str] | None:
        for user in self.user_map:
            if user["id"] == id:
                return user
        return None

class UserRepoProvider(Provider):
    @provide(scope=Scope.APP)
    def create_user_repo(self) -> UserRepo:
        return UserRepoLocal()