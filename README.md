# FAQ Chatbot
This project is a simple FAQ chatbot built with Streamlit, spaCy, and scikit-learn. It uses TF-IDF vectorization and cosine similarity to find the best matching answer to user questions from a predefined FAQ dataset.

## Features
* Preprocesses user queries with spaCy (lemmatization, stopword and punctuation removal).

* Matches user queries with FAQ questions using TF-IDF and cosine similarity.

* Returns the most relevant FAQ answer or a default response if no good match is found.

* Simple, interactive web interface powered by Streamlit.


## Usage
1- Make sure the faq_data.json file is in the project directory with your FAQ question-answer pairs.

2- Run the Streamlit app:

streamlit run app.py

## Code Overview
* FAQs.py — main Streamlit app script.

* faq_data.json — JSON file containing the FAQ questions as keys and answers as values.

* The app preprocesses questions and user input, then finds the closest matching FAQ question using TF-IDF and cosine similarity.

* If no good match is found, it returns a default message asking to rephrase.

## FAQ Data Format
The faq_data.json should be a JSON object with questions as keys and answers as values, for example:

json
Copy code
{
  "How do I place an order?": "Browse the products, add items to your cart, then proceed to checkout to complete your order.",
  "Can I order without creating an account?": "No, creating an account helps us process orders and provide updates efficiently."
}
## Dependencies
* Python 3.7+

* streamlit

* spacy

* scikit-learn