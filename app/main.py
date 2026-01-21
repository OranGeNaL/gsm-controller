from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka
from app.endpoints import users
from app.container import lifespan, get_container


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)

setup_dishka(container=get_container(), app=app)

@app.get("/")
def root():
    return {"message": "Приложение работает!"}
