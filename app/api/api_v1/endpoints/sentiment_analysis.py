from fastapi import APIRouter, Form, Response, Request
from app.sentiment_analyser.sentiment_analyser import vader_analysis
from typing import Any
router = APIRouter()

@router.post("/sentiment", response_model=str, description = "Sentiment Analysis")
async def healthcheck(
    htppRequest: Request,
    httpResponse: Response,
    text: str = Form(
       description="Text to be analysis"
    )
):
    result = vader_analysis(text)

    return f"{result[0]}"