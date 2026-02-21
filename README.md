#  Fraud Detection using XGBoost

## Project Overview
This project builds a fraud detection system using the PaySim synthetic transaction dataset.

The model predicts whether a transaction is fraudulent based on:
- Transaction type
- Amount
- Sender balance
- Receiver balance

## Model Used
XGBoost Classifier

Why XGBoost?
- Handles class imbalance well
- Captures non-linear fraud patterns
- Achieved ROC-AUC of 0.9995

##  Model Performance

| Metric | Value |
|--------|--------|
| ROC-AUC | 0.9995 |
| Fraud Recall | 0.99 |
| Fraud Precision | 0.45 |

## Tech Stack
- Python
- Scikit-learn
- XGBoost
- Streamlit

##  Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
