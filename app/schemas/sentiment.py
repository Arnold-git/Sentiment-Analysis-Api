from pydantic import BaseModel

class SentimentResult(BaseModel):
    sentiment: str
    polarity_score: float