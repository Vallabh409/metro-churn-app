"""
Metro Customer Churn Prediction App

This Streamlit app allows users to input customer details and predicts the likelihood of churn
using a pre-trained machine learning model.
"""

import streamlit as st
import pandas as pd
import pickle

# Set page configuration
st.set_page_config(page_title="Metro Churn Prediction", page_icon="🚇")

@st.cache_resource
def load_model():
    """Load the pre-trained model from the pickle file."""
    with open("metro_churn_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("🚇 Metro Customer Churn Prediction")
st.write("Enter customer details below to predict whether the customer is likely to churn.")

# Input fields
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0)
total = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0)
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "None"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer"])
phone = st.selectbox("Phone Service", ["Yes", "No"])

if st.button("Predict Churn"):
    input_df = pd.DataFrame([{
        "Tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "InternetService": internet,
        "Contract": contract,
        "PaymentMethod": payment,
        "PhoneService": phone
    }])
    
    try:
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.error("Prediction: Churn (High Risk)")
        else:
            st.success("Prediction: No Churn (Low Risk)")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
