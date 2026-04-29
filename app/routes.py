from .auth import hash_senha, verificar_senha, criar_token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models
from . import schemas
from jose import jwt, JWTError
from .auth import hash_senha, verificar_senha, criar_token, SECRET_KEY, ALGORITHM


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        return username
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        print("TOKEN RECEBIDO:", token)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Placeholder: verificar usuário fixo (substitua por lógica real)
    if form_data.username != "admin" or not verificar_senha(form_data.password, hash_senha("password")):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
    access_token = criar_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/clientes")
def criar_cliente(nome: str, tipo: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    descontos = {
        "novo": 0,
        "fidelizado": 5,
        "premium": 10
    }

    cliente = models.Cliente(
        nome=nome,
        tipo=tipo,
        desconto=descontos.get(tipo.lower(), 0)
    )

    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    return cliente

@router.get("/clientes", response_model=list[schemas.ClienteResponse])
def listar_clientes(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return db.query(models.Cliente).all()

@router.post("/usuarios")
def criar_usuario(username: str, senha: str, db: Session = Depends(get_db)):
    
    usuario_existente = db.query(models.Usuario).filter(
        models.Usuario.username == username
    ).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    usuario = models.Usuario(
        username=username,
        senha=hash_senha(senha)
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return {"msg": "Usuário criado"}

@router.post("/login")
def login(username: str, senha: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.username == username).first()

    if not usuario or not verificar_senha(senha, usuario.senha):
        return {"erro": "Credenciais inválidas"}

    token = criar_token({"sub": usuario.username})

    return {"access_token": token, "token_type": "bearer"}
    
@router.put("/clientes/{cliente_id}")
def atualizar_cliente(
    cliente_id: int,
    nome: str,
    tipo: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    descontos = {
        "novo": 0,
        "fidelizado": 5,
        "premium": 10
    }

    cliente.nome = nome
    cliente.tipo = tipo
    cliente.desconto = descontos.get(tipo.lower(), 0)

    db.commit()
    db.refresh(cliente)

    return cliente

@router.delete("/clientes/{cliente_id}")
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(cliente)
    db.commit()

    return {"msg": "Cliente deletado com sucesso"}

@router.get("/clientes", response_model=list[schemas.ClienteResponse])
def listar_clientes(
    skip: int = 0,
    limit: int = 10,
    tipo: str = None,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    query = db.query(models.Cliente)

    if tipo:
        query = query.filter(models.Cliente.tipo == tipo)

    clientes = query.offset(skip).limit(limit).all()

    return clientes