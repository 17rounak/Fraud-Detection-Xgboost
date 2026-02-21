%%writefile app.py
import streamlit as st
import pandas as pd
import joblib

# Load model + threshold
artifacts = joblib.load("xgboost_model.pkl")
model = artifacts["model"]
THRESHOLD = artifacts["threshold"]

st.title("💳 Fraud Detection App")

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT"]
)


amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old balance (Sender)", min_value=0.0, value=5000.0)
newbalanceOrig = st.number_input("New balance (Sender)", min_value=0.0, value=4000.0)
oldbalanceDest = st.number_input("Old balance (Receiver)", min_value=0.0, value=2000.0)
newbalanceDest = st.number_input("New balance (Receiver)", min_value=0.0, value=3000.0)

if st.button("Check Fraud"):
    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })

    prob = model.predict_proba(input_data)[0][1]

    st.write(f"Fraud Probability: {prob:.4f}")

    if prob >= THRESHOLD:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Legit Transaction")
