from fastapi import APIRouter
from app.config import settings
router = APIRouter()

@router.get("/health", response_model=str, description = "health check")
def healthcheck() -> str:
    return f"{settings.PROJECT_NAME} Service is up and running"