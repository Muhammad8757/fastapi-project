from abc import ABC
from typing import Generic
from sqlalchemy.orm import Session
from src.base.abstracts.models import db
from src.base.abstracts.types import TCreateDTO, TModel, TUpdateDTO

class AbstractGenericClass(ABC, Generic[TModel]):
    pass

class AbstractRepository(AbstractGenericClass[TModel]):
    def __init__(self, model: type[TModel]):
        self.model = model

    def get_model(self) -> type[TModel]:
        return self.model
    
    def create(self, dto: TCreateDTO):
        obj = self.model(**dto.model_dump())
        db.add(obj)
        self._commit()
        return obj
    
    def get(self, *args, **kwargs):
        return db.query(self.model).get(**kwargs)
    
    def all(self, *args, **kwargs):
        return db.query(self.model).all()
    
    def filter(self, *args, **kwargs):
        return db.query(self.model).filter_by(**kwargs).all()
    
    def update(self, obj: TModel, dto: TUpdateDTO):
        for key, value in dto.model_dump().items():
            setattr(obj, key, value)
        self._commit()
        self._refresh()
        return obj
    
    def delete(self, obj: TModel):
        db.delete(obj)
        self._commit()
        return obj

    def _commit(self, ):
        return db.commit()
    
    def _refresh(self):
        return db.refresh()
    
    def execute(self, db: Session, *args, **kwargs):
        pass