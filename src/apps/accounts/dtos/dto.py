from src.base.abstracts.dto import ModelDto
from pydantic import Field

class UserCreateDto(ModelDto):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=3, max_length=50)


class UserUpdateDto(ModelDto):
    username: str | None = None
    email: str | None = None
    password: str | None = None