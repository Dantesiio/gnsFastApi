"""Minimal FastAPI application used during interview practice sessions."""
from fastapi import FastAPI

# Usa importaciones relativas para resolver el paquete.
from .api.users import router as users_router

# Creating the FastAPI instance is the entry point for the web application.
app = FastAPI(
    title="GNS Interview Practice API",
    description="Simple endpoints to practice FastAPI fundamentals.",
    version="0.2.0",
)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Basic endpoint to verify the service is running."""
    return {"status": "ok"}


# Routers help keep endpoints organized as the project grows.
app.include_router(users_router, prefix="/api", tags=["users"])
