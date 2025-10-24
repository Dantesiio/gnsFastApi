"""API de Usuarios MUY sencilla para principiantes.

Qué hace:
- Guarda usuarios en una lista en memoria (no hay base de datos).
- Tiene 3 endpoints básicos: GET (listar), POST (crear) y DELETE (borrar).
- Usa un solo modelo `User` para validar datos.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    # id es opcional al crear; el servidor lo asignará automáticamente.
    id: int | None = None
    name: str
    email: str


router = APIRouter()

# "Base de datos" simple: solo una lista de usuarios en memoria.
USERS: list[User] = []


def _next_id() -> int:
    # Si no hay usuarios, empieza en 1; si hay, toma el máximo y suma 1.
    return (max([u.id or 0 for u in USERS]) + 1) if USERS else 1


@router.get("/users")
def list_users() -> list[User]:
    """Devuelve la lista completa de usuarios."""
    return USERS


@router.post("/users", status_code=201)
def create_user(user: User) -> User:
    """Crea un usuario nuevo.

    - Si no envías `id`, el servidor lo pone automáticamente.
    - Solo se validan tipos básicos (name/email como texto).
    """
    new_user = User(id=user.id or _next_id(), name=user.name, email=user.email)
    USERS.append(new_user)
    return new_user


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int) -> None:
    """Borra un usuario por su `id`.

    - Si no existe, devuelve un error 404.
    - Si existe, lo quita de la lista y no devuelve contenido.
    """
    for idx, u in enumerate(USERS):
        if u.id == user_id:
            USERS.pop(idx)
            return None
    raise HTTPException(status_code=404, detail="User not found")
