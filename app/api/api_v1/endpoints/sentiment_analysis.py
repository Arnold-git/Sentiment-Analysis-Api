from fastapi import APIRouter, Form, Response, Request
from app.schemas.error import ServiceError
from app.schemas.response import SentimentResponse
from app.sentiment_analyser.sentiment_analyser import vader_analysis
from typing import Any
router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse, description = "Sentiment Analysis")
async def healthcheck(
    httpResponse: Response,
    text: str = Form(
       description="Text to be analysis" 
    )
):
    try:
        result = vader_analysis(text)

        response = SentimentResponse(
            success = True,
            data = result
        )
        return response

    except ServiceError as e:
        httpResponse.status_code = 400
        response = SentimentResponse(
            success = False,
            message = e.meesage
        )

        return response