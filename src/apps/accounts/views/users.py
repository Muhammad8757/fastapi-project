from src.base.abstracts.app import app
from src.apps.accounts.dtos.dto import UserCreateDto
from src.apps.accounts.services.users import user_service

@app.post("/register")
def register(user: UserCreateDto):
    return user_service.create(user)