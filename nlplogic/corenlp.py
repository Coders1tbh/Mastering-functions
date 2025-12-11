import wikipedia
from textblob import TextBlob


def search_wikipedia(name):
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize the Wikipedia article for the given name."""
    print(f"Summarizing for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Return a TextBlob object from text."""
    return TextBlob(text)


def get_phrases(name):
    """Return noun phrases from the Wikipedia summary."""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    return blob.noun_phrases
