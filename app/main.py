import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.api.api_v1.api import api_router
from app.config import settings


def customise_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema



    openapi_schema = get_openapi(
        title="SentimentApi",
        version="1.0",
        description="SentimentApi",
        routes=app.routes,
        servers=None
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)
customise_openapi(app)