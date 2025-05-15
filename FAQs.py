import streamlit as st
import json
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

with open("faq_data.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)
    
questions = list(faq_data.keys())
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

processed = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed)

def get_response(query):
    cleaned = preprocess(query)
    user_vec = vectorizer.transform([cleaned])
    sims = cosine_similarity(user_vec, tfidf_matrix).flatten()
    idx = sims.argmax()
    return faq_data[questions[idx]] if sims[idx] > 0.3 else "Sorry, I couldn't understand. Try rephrasing."

# Streamlit interface
st.title("FAQ Chatbot")
user_input = st.text_input("Ask your question:")
if user_input:
    answer = get_response(user_input)
    st.write("Bot:", answer)