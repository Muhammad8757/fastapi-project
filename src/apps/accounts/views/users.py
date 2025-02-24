from src.base.abstracts.app import app
from src.apps.accounts.dtos.dto import UserCreateDto
from src.apps.accounts.services.users import user_service
from fastapi import Response

@app.post("/register")
def register(user: UserCreateDto):
    user = user_service.create(user)
    return Response(status_code=201)