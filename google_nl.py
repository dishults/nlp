'''
That's where magic happens :)
Google Cloud Natural Language API that analyzes sentiment
'''

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import types

def analyze_sentiment(text):
    "Returns sentiment"
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The file to analyze
    document = types.Document(
        content=text,
        type='PLAIN_TEXT')

    # Detects the sentiment of the text
    sen = client.analyze_sentiment(document=document).document_sentiment

    return sen
    