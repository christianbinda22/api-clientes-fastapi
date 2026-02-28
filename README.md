 🧱 Sales Management API

API RESTful para gerenciamento de vendas, clientes, produtos e pedidos.
Projeto desenvolvido com foco em boas práticas de arquitetura backend, autenticação segura e modelagem relacional com SQLAlchemy.

---

## 📌 Visão Geral

Esta API simula um sistema interno de controle de vendas para uma empresa de gesso 3D.

O sistema permite:

- Gerenciamento de clientes
- Cadastro de usuários (funcionários)
- Controle de produtos e estoque
- Criação de pedidos com múltiplos itens
- Cálculo de valor total automaticamente
- Autenticação via JWT
- Controle de permissões (admin)

---

## 🏗 Arquitetura

O projeto segue separação em camadas:

- `models` → Mapeamento ORM (SQLAlchemy)
- `schemas` → Validação de dados (Pydantic)
- `routers` → Endpoints organizados por domínio
- `services` → Regras de negócio
- `database` → Conexão e sessão do banco

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- FastAPI
- SQLAlchemy ORM
- JWT Authentication
- SQLite (dev) / PostgreSQL (produção-ready)
- Uvicorn

---

## 🔐 Autenticação

A autenticação é feita via JWT.

### Fluxo:

1. Login com username e senha
2. Retorno de access_token
3. Envio do token no header:

Authorization: Bearer {token}

---

## 🗂 Modelagem do Banco

### Entidades principais

Cliente → Pedido → ItemPedido → Produto  
Usuario → Pedido

Relacionamentos implementados com `relationship()` e `ForeignKey`.

---

## ▶️ Executando o Projeto

```bash
git clone <repo>
cd projeto_api
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
📄 Documentação Interativa

Swagger:
http://localhost:8000/docs

Redoc:
http://localhost:8000/redoc

📌 Melhorias Futuras

Paginação

Filtros avançados

Logs estruturados

Testes automatizados (Pytest)

Dockerização

Deploy em cloud

👨‍💻 Autor

Christian Binda
Backend Developer