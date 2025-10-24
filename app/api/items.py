"""Endpoints de Items para la prueba técnica.

Requisitos que cubre:
- POST /items: crea un ítem con `name` y `price`.
- GET /items: devuelve todos los ítems guardados.
- GET /items/{id}: devuelve un ítem por su id (opcional en el enunciado).

La "base de datos" es una lista en memoria para mantenerlo simple.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int | None = None
    name: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)


router = APIRouter()

# Almacenamiento en memoria
ITEMS: list[Item] = []


def _next_id() -> int:
    return (max([i.id or 0 for i in ITEMS]) + 1) if ITEMS else 1


@router.post("/items", status_code=201)
def create_item(item: Item) -> Item:
    """Crea un nuevo ítem y lo devuelve con su `id` asignado."""
    new_item = Item(id=item.id or _next_id(), name=item.name, price=item.price)
    ITEMS.append(new_item)
    return new_item


@router.get("/items")
def list_items() -> list[Item]:
    """Devuelve todos los ítems guardados."""
    return ITEMS


@router.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    """Devuelve un ítem por su `id` o 404 si no existe."""
    for it in ITEMS:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")
