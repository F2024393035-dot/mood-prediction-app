import streamlit as st
import re

# --- Text cleaning function ---
def clean_text(text):
    text = text.strip()                  # Remove leading/trailing spaces
    text = re.sub('\s+', ' ', text)     # Replace multiple spaces with a single space
    text = text.lower()                 # Convert text to lowercase
    return text

# --- Mood prediction logic ---
def predict_mood(text):
    cleaned = clean_text(text)
    
    happy_words = ["happy", "joy", "excited", "great", "love", "good"]
    sad_words = ["sad", "bad", "angry", "upset", "tired", "hate"]
    
    if any(word in cleaned for word in happy_words):
        return "Happy 😊"
    elif any(word in cleaned for word in sad_words):
        return "Sad 😢"
    else:
        return "Neutral 😐"

# --- Streamlit App Interface ---
st.title("🧠 Mood Prediction App")
st.write("Describe how you're feeling, and let the model guess your mood!")

# User input
user_input = st.text_area("How are you feeling today?", "")

# Prediction
if st.button("Predict Mood"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze your mood.")
    else:
        mood = predict_mood(user_input)
        st.success(f"Predicted Mood: **{mood}**")
