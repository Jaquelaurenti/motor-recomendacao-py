from fastapi import FastAPI
from app.interfaces.api.routes import router

app = FastAPI(title="Recommender System API")

app.include_router(router)