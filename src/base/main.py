from fastapi import FastAPI
from src.base.app import app
from src.base.engine import engine
from src.base.models import Base

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API летает, братик!"}
