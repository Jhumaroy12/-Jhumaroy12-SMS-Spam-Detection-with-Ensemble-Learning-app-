import streamlit as st
import joblib

with open('spam_classifier.pkl', 'rb') as f:
    model = joblib.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = joblib.load(f)


def preprocess_text(text):
   
    return text

st.title("SMS Spam Classifier")
st.write("Enter your SMS message below to classify it as **Spam** or **ham**.")


user_input = st.text_area("SMS Message:", "")

if st.button("Predict"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid SMS message.")
    else:
      
        processed_text = preprocess_text(user_input)

    
        vectorized_text = vectorizer.transform([processed_text]).toarray()  

      
        prediction = model.predict(vectorized_text)[0]

       
        if prediction == 1:  
            st.error(" This message is **SPAM**.")
        else:
            st.success("This message is **NOT SPAM(ham)**. Safe!")

st.markdown("---")

