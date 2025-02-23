from sqlalchemy import create_engine
from src.configs.settings.base import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})