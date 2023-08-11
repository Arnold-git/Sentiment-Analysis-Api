from fastapi import APIRouter, Response
from app.schemas.error import ServiceError
from app.schemas.response import SentimentResponse
from app.schemas.input_data import ExampleText
from app.sentiment_analyser.sentiment_analyser import vader_analysis
from loguru import logger

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse, description = "Sentiment Analysis")
def sentiment_analysis(
    httpResponse: Response,
    text: ExampleText
):
    try:
        logger.info(f"Making prediction for input text: {text}")
        result = vader_analysis(text)
        logger.info(f"Prediction result: {result}")

        response = SentimentResponse(
            success = True,
            data = result
        )

        return response

    except ServiceError as e:
        httpResponse.status_code = 400
        logger.warning(f"Prediction error: {e}")
        response = SentimentResponse(
            success = False,
            message = e.meesage
        )

        return response