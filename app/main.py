from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.config import settings
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])