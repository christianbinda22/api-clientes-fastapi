from fastapi import FastAPI
from .database import engine, Base
from .routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

from fastapi import FastAPI

app = FastAPI(
    title="Sales Management API",
    description="""
API REST para gerenciamento de vendas.

Features:
- CRUD de clientes
- CRUD de produtos
- Criação de pedidos com múltiplos itens
- Controle de estoque
- Autenticação JWT
""",
    version="1.0.0",
    contact={
        "name": "Christian Binda",
        "url": "https://github.com/christianbinda22",
    },
    license_info={
        "name": "B!NDEV",
    },
)