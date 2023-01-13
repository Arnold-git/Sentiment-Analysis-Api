from helpers.clean_text import clean_text
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def vader_analysis(text):
    """
    Helper function to get sentiment using vader rule based sentiment analysis libary
    Returns:
        sentiment category -> positive, negative or neutral
    """
    clean_text = clean_text(text)

    compound = analyzer.polarity_scores(clean_text)['compound']
    if compound >= 0.5:
        return 'Positive'
    elif compound <= -0.5 :
        return 'Negative'
    else:
        return 'Neutral'


