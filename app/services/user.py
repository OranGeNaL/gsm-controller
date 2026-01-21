from typing import Protocol
from dishka import make_async_container, Provider, provide, Scope

from app.repositories.user import UserRepo

class UserService(Protocol):
    def get_by_id(self, id) -> dict[str,  str] | None:
        ...

class UserServiceImpl(UserService):
    def __init__(self, repo: UserRepo):
        self.repo = repo
        
    def get_by_id(self, id):
        return self.repo.by_id(id)