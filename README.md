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

## Dataset
This project uses the **PaySim Synthetic Financial Dataset**.
Due to its large size (~6M+ transactions), the dataset is not included in this repository.

You can download it from Kaggle:
https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

##  Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
