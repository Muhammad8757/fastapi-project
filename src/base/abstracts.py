from abc import ABC
from typing import Generic, TypeVar
from sqlalchemy.orm import DeclarativeBase
from src.base.models import db
from sqlalchemy.orm import Session



TModel = TypeVar("TModel", bound=DeclarativeBase)

class AbstractGenericClass(ABC, Generic[TModel]):
    pass

class AbstractRepository(AbstractGenericClass[TModel]):
    def __init__(self, model: type[TModel]):
        self.model = model

    def get_model(self) -> type[TModel]:
        return self.model
    
    def create(self, data: tuple):
        obj = self.model(**data)
        db.add(obj)
        self._commit(db)
        self._refresh(db)
        return obj


    def _commit(self, db: Session):
        return db.commit()
    
    def _refresh(self, db: Session):
        return db.refresh()