from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.types import Numeric   
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    telefone = Column(String, nullable=True)
    desconto = Column(Numeric(5,2), default=0)

    pedidos = relationship("Pedido", back_populates="cliente")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)

    pedidos = relationship("Pedido", back_populates="usuario")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    descricao = Column(String)
    preco = Column(Numeric(10,2), nullable=False)
    estoque = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)

    itens = relationship("ItemPedido", back_populates="produto")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    valor_total = Column(Numeric(10,2), nullable=False)

    cliente = relationship("Cliente", back_populates="pedidos")
    usuario = relationship("Usuario", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)

    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Numeric(10,2), nullable=False)

    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto", back_populates="itens")

    created_at = Column(DateTime(timezone=True), server_default=func.now())