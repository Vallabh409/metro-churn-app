
import streamlit as st
import pandas as pd
import pickle

# Load the model
with open("metro_churn_model.pkl", "rb") as f:
    model = pickle.load(f)

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

    prediction = model.predict(input_df)[0]
    st.success(f"Prediction: {'Churn' if prediction == 1 else 'No Churn'}")
