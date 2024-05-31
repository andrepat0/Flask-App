from transformers import pipeline

def load_model():
    return pipeline('sentiment-analysis')

model = load_model()

def analyze_sentiment(text):
    return model(text)