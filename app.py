
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Load the trained model
@st.cache_resource
def load_model():
    if os.path.exists("model.pkl"):
        with open("model.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return None

model = load_model()

st.title("🔍 Fraud Detection App")

# Input fields
amount = st.number_input("Enter transaction amount:", min_value=0.0)
transaction_time = st.slider("Enter transaction time (hour 0-23):", 0, 23, 12)
user_age = st.number_input("Enter user's age:", min_value=18, max_value=100, value=30)

# Create input data for prediction
input_data = np.array([[amount, transaction_time, user_age]])

# Make prediction when button is clicked
if st.button("Predict"):
    if model is None:
        st.warning("⚠️ Model file not found. Please upload or add 'model.pkl' to this directory.")
    else:
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("🚨 ALERT: This transaction is predicted as FRAUD!") 
        else:
            st.success("✅ This transaction is predicted as NOT FRAUD.")

    if prediction == 1:
        st.error("🚨 ALERT: This transaction is predicted as FRAUD!") 
    else:
        st.success("✅ This transaction is predicted as NOT FRAUD.")
