import streamlit as st
import joblib
import gdown
import os

# === Function to download files from Google Drive ===
def download_file_from_gdrive(file_id, output_path):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_path, quiet=False)

# === Load spam_classifier.pkl ===
spam_model_path = "spam_classifier.pkl"
if not os.path.exists(spam_model_path):
    download_file_from_gdrive("1TAeLevAJdhI0WUOpze81AK31m6L8UDUj", spam_model_path)
model = joblib.load(spam_model_path)

# === Load tfidf_vectorizer.pkl ===
vectorizer_path = "tfidf_vectorizer.pkl"
if not os.path.exists(vectorizer_path):
    download_file_from_gdrive("1ugeTX33Lbw324Dj5PHIDGYsHS_cG8WaN", vectorizer_path)
vectorizer = joblib.load(vectorizer_path)

# === Optional Preprocessing Function ===
def preprocess_text(text):
    # You can add text cleaning here if needed
    return text

# === Streamlit App UI ===
st.title(" SMS Spam Classifier")
st.write("Enter your SMS message below to classify it as **Spam** or **Ham (Not Spam)**.")

user_input = st.text_area(" SMS Message:", "")

if st.button("Predict"):
    if not user_input.strip():
        st.warning(" Please enter a valid SMS message.")
    else:
        # Preprocess input
        processed_text = preprocess_text(user_input)

        # Vectorize input
        vectorized_text = vectorizer.transform([processed_text]).toarray()

        # Make prediction
        prediction = model.predict(vectorized_text)[0]

        # Show result
        if prediction == 1:  
            st.error(" This message is **SPAM**.")
        else:
            st.success(" This message is **NOT SPAM (Ham)**. Safe!")

st.markdown("---")
