from src.base.abstracts.dto import ModelDto
from pydantic import Field

class UserCreateDto(ModelDto):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=100)

class UserUpdateDto(ModelDto):
    name: str | None = None
    age: int | None = None
