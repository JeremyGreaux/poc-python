from fastapi import FastAPI

from app import api
from sql_app import models
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api.api_router)