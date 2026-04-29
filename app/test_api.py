import requests

BASE_URL = "http://127.0.0.1:8000"

print("Criando usuário...")
requests.post(f"{BASE_URL}/usuarios", params={
    "username": "admin",
    "senha": "123"
})

print("Fazendo login...")
res = requests.post(f"{BASE_URL}/login", params={
    "username": "admin",
    "senha": "123"
})

print("Resposta login:", res.text)

token = res.json().get("access_token")

if not token:
    print("Token não encontrado, parando execução.")
    exit()

# 🔥 AQUI ESTÁ O SEGREDO
headers = {
    "Authorization": f"Bearer {token}"
}

print("Criando cliente...")
res = requests.post(
    f"{BASE_URL}/clientes",
    params={"nome": "João", "tipo": "premium"},
    headers=headers
)

print("Status:", res.status_code)
print("Resposta:", res.text)

print("Listando clientes...")
res = requests.get(
    f"{BASE_URL}/clientes",
    headers=headers
)

print("Status:", res.status_code)
print("Resposta:", res.text)