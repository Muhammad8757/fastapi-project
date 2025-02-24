from typing import TypeVar
from src.base.abstracts.models import Base
from pydantic import BaseModel



TModel = TypeVar("TModel", bound=Base)
TCreateDTO = TypeVar("TCreateDTO", bound=BaseModel)
TUpdateDTO = TypeVar("TUpdateDTO", bound=BaseModel)
