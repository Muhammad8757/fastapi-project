from typing import Generic, Union

from src.base.abstracts.repositories import AbstractRepository
from src.base.abstracts.types import TCreateDTO, TModel, TUpdateDTO


class AbstractFetchService(Generic[TModel]):
    def __init__(self, repository: Union[AbstractRepository[TModel]]):
        self._repository = repository
    
    @property
    def model(self):
        return self._repository.get_model()
    
    def get(self, *args, **kwargs):
        return self._repository.get(*args, **kwargs)
    
    def all(self, *args, **kwargs):
        return self._repository.all(*args, **kwargs)
    
    def filter(self, *args, **kwargs):
        return self._repository.filter(*args, **kwargs)
    
    def execute(self, *args, **kwargs):
        return self._repository.execute(*args, **kwargs)


class AbstractCRUDService(Generic[TModel]):
    def __init__(self, repository: Union[AbstractRepository[TModel]]):
        self._repository = repository

    @property
    def model(self):
        return self._repository.get_model()

    def create(self, dto: TCreateDTO):
        return self._repository.create(dto=dto)

    def update(self, obj: TModel, dto: TUpdateDTO):
        return self._repository.update(obj, dto)

    def delete(self, obj: TModel):
        return self._repository.delete(obj)

    def execute(self, *args, **kwargs):
        return self._repository.execute(*args, **kwargs)

