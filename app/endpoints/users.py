from fastapi import APIRouter
from loguru import logger

from app.services.user import UserService

from dishka.integrations.fastapi import (
    DishkaRoute,
    FromDishka,
    FastapiProvider,
    inject,
    setup_dishka,
)
from dishka import make_async_container, Provider, provide, Scope

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    route_class=DishkaRoute
)

@router.get("/")
def get_users() -> list[dict]:
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/me")
def get_current_user() -> dict:
    logger.info("/me call")
    return {"username": "Rick", "role": "admin"}

@router.get("/by_id")
def get_user_by_id(service: FromDishka[UserService]) -> dict[str, str] | None:
    logger.info("/by_id call")
    return service.get_by_id("1")