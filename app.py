import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the brain for the AI
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

st.title("🛍️ Product Recommendation AI")
user_input = st.text_input("Enter your product review here:")

if user_input:
    score = sia.polarity_scores(user_input)['compound']
    if score >= 0.05:
        st.success(f"Sentiment Score: {score} | VERDICT: Recommended! 🌟")
    elif score <= -0.05:
        st.error(f"Sentiment Score: {score} | VERDICT: Do Not Buy! ⚠️")
    else:
        st.info(f"Sentiment Score: {score} | VERDICT: Neutral ⚖️")
