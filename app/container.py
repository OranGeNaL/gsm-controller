from fastapi import FastAPI
from loguru import logger
from dishka.integrations.fastapi import FastapiProvider

from dishka import make_async_container, Provider, provide, Scope

from contextlib import asynccontextmanager
from app.services.user import UserService, UserServiceImpl
from app.repositories.user import UserRepo, UserRepoProvider

class UserServiceProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_user_service(self) -> UserService:
        user_repo = await get_container().get(UserRepo)
        logger.info("received user_repo")
        return UserServiceImpl(repo=user_repo)

container = make_async_container(
    UserRepoProvider(),
    UserServiceProvider(),
    FastapiProvider())

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def get_container():
    return container