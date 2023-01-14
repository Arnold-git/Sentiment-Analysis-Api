from fastapi import APIRouter
from app.api.api_v1.endpoints import health
from app.api.api_v1.endpoints import sentiment_analysis
api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(sentiment_analysis.router, tags=["Sentiment Analysis"])