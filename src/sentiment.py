from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


def analyze_headlines(headlines):
    results = []
    for headline in headlines:
        sentiment_score = analyze_sentiment(headline)
        results.append({"headline": headline, "sentiment": sentiment_score})
    return results
