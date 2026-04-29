from pydantic import BaseModel


class ClienteBase(BaseModel):
    nome: str
    tipo: str


class ClienteCreate(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    id: int
    desconto: int

    class Config:
        orm_mode = True