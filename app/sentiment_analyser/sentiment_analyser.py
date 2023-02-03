from app.helpers.clean_text import clean_text
from app.schemas.sentiment import SentimentResult
from app.schemas.error import ServiceError
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def vader_analysis(text):
    """
    Helper function to get sentiment using vader rule based sentiment analysis libary
    Returns:
        sentiment category -> positive, negative or neutral
    """
    preprocessed_text = clean_text(text)

    raw_cat = analyzer.polarity_scores(preprocessed_text)
    
    compound = round(analyzer.polarity_scores(preprocessed_text)['compound'], 2)
    try: 
        if compound >= 0.5:
            sentiment_result = SentimentResult(
                sentiment = "Positive",
                polarity_score = compound,
                raw_categorisation = raw_cat
                )
            return sentiment_result
        elif compound <= -0.5:
            sentiment_result = SentimentResult(
                sentiment = "Negative",
                polarity_score = compound,
                raw_categorisation = raw_cat
                )
            return sentiment_result
        else:
            sentiment_result = SentimentResult(
                sentiment = "Neutral",
                polarity_score = compound,
                raw_categorisation = raw_cat
                )
                
            return sentiment_result
        
    except Exception:
        return ServiceError("Sentiment Analysis was unsuccessful")


