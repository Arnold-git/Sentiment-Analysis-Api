from typing import Any

from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.api.api_v1.api import api_router
from app.config import settings
from loguru import logger
import uvicorn

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


root_router = APIRouter()

@root_router.get("/")
def index(request: Request) -> Any:
    """
    Basic HTML response
    """
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to Sentiment Analysis Prediction API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)

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
app.include_router(root_router)
customise_openapi(app)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)