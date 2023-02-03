from pydantic import BaseModel

class SentimentResult(BaseModel):
    sentiment: str
    polarity_score: float
    raw_categorisation: dict