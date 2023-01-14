from app.schemas.sentiment import SentimentResult
from typing import Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    success: bool
    message: Optional[str]

class SentimentResponse(BaseResponse):
    data: Optional[SentimentResult]