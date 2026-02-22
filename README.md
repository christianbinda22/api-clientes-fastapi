API de Clientes - FastAPI

API REST desenvolvida com Python + FastAPI para gerenciamento de usuários e clientes, com autenticação JWT e rotas protegidas.

📌 Sobre o projeto

Este projeto foi criado com foco em práticas reais de desenvolvimento Back-End:

Estrutura modular

Autenticação com JWT

CRUD completo

Integração com banco de dados

Proteção de rotas

Organização em camadas

Projeto desenvolvido como parte da formação prática para atuação como Desenvolvedor Back-End Python.

🚀 Tecnologias utilizadas

Python 3

FastAPI

SQLAlchemy

SQLite / MySQL

Uvicorn

JWT (Autenticação)

Git & GitHub

📂 Estrutura do projeto
api-clientes-fastapi/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── database.py
│   ├── auth.py
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Como executar o projeto
1. Clonar o repositório
git clone https://github.com/christianbinda22/api-clientes-fastapi.git
cd api-clientes-fastapi
2. Criar ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Executar o servidor
uvicorn app.main:app --reload

Acesse a documentação automática:

http://127.0.0.1:8000/docs
🔐 Autenticação

Criar usuário

Fazer login

Copiar o token

Clicar em Authorize no Swagger

Usar o token nas rotas protegidas

📌 Funcionalidades

Cadastro de usuários

Login com JWT

Criação de clientes

Listagem de clientes

Descontos por tipo:

Novo: 0%

Fidelizado: 5%

Premium: 10%

📈 Próximas melhorias (Roadmap)

Validação com Pydantic

Testes automatizados (Pytest)

Docker

Deploy em cloud

Paginação e filtros

👨‍💻 Autor

Christian Binda
Desenvolvedor Back-End Python
Buscando oportunidade como Desenvolvedor Júnior

GitHub: https://github.com/christianbinda22
