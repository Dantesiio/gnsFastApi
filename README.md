# GNS FastAPI Interview Practice

Mini API REST para practicar FastAPI durante la prueba técnica. Incluye endpoints de usuarios y los ítems solicitados en el enunciado.

## Requisitos

- Python 3.12+
- pip
- Docker y Docker Compose

Instala dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Arranca el servidor:

```bash
docker compose up 
```

y 
```bash
docker build -t gnsfastapi:latest .
```

Swagger UI disponible en `http://127.0.0.1:8000/docs`.

## Endpoints Clave

### Items API

- `POST /items` → Crea ítem `{ "name": str, "price": float }`
- `GET /items` → Lista todos los ítems
- `GET /items/{id}` → Recupera un ítem por id

Prueba rápida:

```bash
curl -X POST http://localhost:8000/items \
  -H 'Content-Type: application/json' \
  -d '{"name":"Laptop","price":100.5}'

curl http://localhost:8000/items
```

### Users API

- `GET /api/users`
- `POST /api/users`
- `DELETE /api/users/{user_id}`.
