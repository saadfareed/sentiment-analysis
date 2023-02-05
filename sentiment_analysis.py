import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

text = "I love this product! It is amazing."
print(sentiment_analysis(text))

text = "I hate this product! It is terrible."
print(sentiment_analysis(text))

text = "This product is okay, not the best but not the worst." 
print(sentiment_analysis(text))
