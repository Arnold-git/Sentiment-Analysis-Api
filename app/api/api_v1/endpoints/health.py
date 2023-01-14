from fastapi import APIRouter
router = APIRouter()

@router.get("/health", response_model=str, description = "health check")
def healthcheck() -> str:
    return "Service is up and running yes"