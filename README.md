# SMS Spam Classifier (Streamlit App)

A web application built with **Streamlit** that classifies SMS messages as **SPAM** or **HAM (Not Spam)** using a machine learning ensemble model trained on SMS text data.

---

## Live Demo

🔗 [Live App on Streamlit Cloud]([https://your-streamlit-url.streamlit.app](https://chtbvxea8n47xpoghh9ggm.streamlit.app/))


##  Project Structure

sms-spam-classifier/
│
├── app.py # Streamlit app file
├── requirements.txt # Python dependencies


> Model files (`spam_classifier.pkl` and `tfidf_vectorizer.pkl`) are loaded from Google Drive at runtime.

---

##  Model Files (Google Drive Links)

- **Spam Classifier Model (.pkl)**  
  🔗 https://drive.google.com/file/d/1TAeLevAJdhI0WUOpze81AK31m6L8UDUj/view?usp=drive_link

- **TF-IDF Vectorizer (.pkl)**  
  🔗 https://drive.google.com/file/d/1ugeTX33Lbw324Dj5PHIDGYsHS_cG8WaN/view?usp=sharing

These files are automatically downloaded when the app runs using the `gdown` library.


## Features
Predict whether an SMS is SPAM or HAM

Clean and simple Streamlit UI

Loads large model files dynamically via Google Drive

Compatible with Streamlit Cloud

 ## Model Info
Feature extraction: TF-IDF Vectorization

Classifier: Ensemble machine learning model

Dataset: SMS Spam Collection dataset

