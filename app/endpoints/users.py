from fastapi import APIRouter

from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users() -> list[dict]:
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/me")
def get_current_user() -> dict:
    return {"username": "Rick", "role": "admin"}

@router.get("/by_id")
def get_user_by_id(service: UserService) -> dict:
    return 