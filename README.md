
# 🧠 Mood Prediction App (NLP + Streamlit)
This is an interactive web app that predicts a person's mood based on their written text (e.g., journal, message, or social media post). It uses a logistic regression model trained on a labeled emotion dataset, and a Streamlit frontend for live interaction.
## 🚀 Features
- Clean and minimal Streamlit UI
- Text input for users to check their mood
- Trained ML model using TF-IDF and Logistic Regression
- Real-time predictions
- Label encoder for decoding mood category
## 📁 Files
- `app.py`: Streamlit app script
- `mood_model.pkl`: Trained Logistic Regression model
- `requirements.txt`: Python dependencies
## 🧪 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
