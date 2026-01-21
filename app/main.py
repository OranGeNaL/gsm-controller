from fastapi import FastAPI
from dishka import Provider, Scope, make_container

from app.endpoints import users

from app.services.user_service import UserService

service_provider = Provider(scope=Scope.APP)
service_provider.provide(UserService)

container = make_container(service_provider)

app = FastAPI(title="GSM Controller")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Приложение работает!"}