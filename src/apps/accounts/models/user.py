from sqlalchemy import Column, Integer, String
from src.base.abstracts.models import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __setattr__(self, name, value):
        from src.apps.accounts.services.users import user_service
        if name == "password":
            value = user_service.get_hash(value)
        super().__setattr__(name, value)