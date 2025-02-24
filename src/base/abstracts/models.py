from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.base.engine import engine
from src.base.abstracts import app

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

app
