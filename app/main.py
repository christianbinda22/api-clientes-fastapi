from fastapi import FastAPI
from .routes import router
from .database import engine, Base

app = FastAPI(
    title="Sales Management API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)  # 👈 ISSO AQUI É O MAIS IMPORTANTE