# Credit-Card Fraud Detection

## Project Overview

This project focuses on detecting fraudulent transactions using machine learning techniques.

The project uses the provided FASTag transaction dataset, which contains transaction details such as vehicle type, toll booth, lane type, transaction amount, amount paid, geographical location, vehicle speed, and fraud status.

The target variable is `Fraud_indicator`, which contains two classes:

- Fraud
- Not Fraud

## Dataset

The dataset contains:

- 5,000 transactions
- 13 original columns
- Target variable: `Fraud_indicator`

The dataset contains some missing values in `FastagID`, which were handled during preprocessing.

## Objectives

- Explore the transaction dataset.
- Analyze the fraud and non-fraud class distribution.
- Perform exploratory data analysis.
- Identify categorical and numerical features.
- Handle the class imbalance using SMOTE.
- Train Random Forest and XGBoost models.
- Evaluate models using Precision, Recall, F1-Score and ROC-AUC.
- Analyze the precision-recall trade-off.
- Study different fraud decision thresholds.
- Save the trained machine learning models for future use.

## Exploratory Data Analysis

The project includes analysis of:

- Fraud vs Not Fraud transactions
- Vehicle speed by fraud status
- Transaction amount by fraud status
- Transaction amount vs amount paid
- Fraud distribution by vehicle type
- Fraud distribution by lane type
- Fraud distribution by vehicle dimensions
- Fraud rate by geographical location
- Fraud rate by hour of the day
- Feature cardinality
- Duplicate transactions

## Class Distribution

The dataset contains:

- Not Fraud: 4,017 transactions
- Fraud: 983 transactions

This represents:

- Not Fraud: 80.34%
- Fraud: 19.66%

Because the classes are imbalanced, SMOTE was applied to the training data.

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the FASTag transaction dataset.
2. Checked dataset shape and information.
3. Checked missing values.
4. Checked duplicate transactions.
5. Converted `Timestamp` into datetime format.
6. Extracted:
   - Hour
   - Day
   - DayOfWeek
7. Selected relevant modelling features.
8. Separated features and target.
9. Identified categorical and numerical features.
10. Applied One-Hot Encoding to categorical features.
11. Split the data into training and testing sets using stratification.
12. Applied SMOTE only to the training data.

## Models

### 1. Random Forest

Two Random Forest models were evaluated:

- Random Forest without SMOTE
- Random Forest with SMOTE

### 2. XGBoost

An XGBoost classifier was trained using the original training data.

## Model Performance

| Model | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|
| Random Forest - Without SMOTE | 1.0000 | 0.9391 | 0.9686 | 0.9994 |
| Random Forest - With SMOTE | 1.0000 | 0.9340 | 0.9659 | 0.9998 |
| XGBoost | 1.0000 | 0.9746 | 0.9871 | 0.9947 |

## XGBoost Confusion Matrix

The XGBoost model produced:

- True Negatives: 803
- False Positives: 0
- False Negatives: 5
- True Positives: 192

Therefore, 192 fraudulent transactions were correctly detected and 5 fraudulent transactions were missed on the test set.

## Precision vs Recall

Different decision thresholds were tested for XGBoost.

At threshold 0.50:

- Precision: 1.0000
- Recall: 0.9746
- F1-Score: 0.9871

At threshold 0.20:

- Precision: 1.0000
- Recall: 0.9848
- F1-Score: 0.9923

At threshold 0.30:

- Precision: 1.0000
- Recall: 0.9848
- F1-Score: 0.9923

The results show that changing the decision threshold affects the balance between precision and recall.

## Business Decision Thresholds

A lower threshold can be considered when detecting more fraudulent transactions is important.

A higher threshold can be considered when reducing unnecessary fraud alerts is more important.

For this test dataset, thresholds of 0.20 and 0.30 produced higher recall and F1-score than the default 0.50 threshold while maintaining 100% precision.

These results are specific to the evaluated test set and should be validated on additional data before deployment.

## Project Structure

```text
Project-2_Credit-Card-Fraud-Detection/
│
├── data/
│   └── FastagFraudDetection.csv
│
├── models/
│   ├── random_forest_model.pkl
│   ├── random_forest_smote_model.pkl
│   ├── xgboost_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   └── fastag_fraud_detection.ipynb
│
├── outputs/
│   ├── business_thresholds.csv
│   ├── confusion_matrix_random_forest.png
│   ├── confusion_matrix_random_forest_smote.png
│   ├── confusion_matrix_xgboost.png
│   ├── model_comparison.csv
│   ├── threshold_analysis.csv
│   └── threshold_analysis.png
│
├── src/
│
├── README.md
└── requirements.txt





##
Conclusion
This project demonstrates a machine learning approach for detecting fraudulent FASTag transactions.
Random Forest and XGBoost were evaluated using precision, recall, F1-score and ROC-AUC. XGBoost achieved a recall of 97.46% and an F1-score of 98.71% at the default threshold of 0.50.
Threshold analysis showed that changing the decision threshold can improve fraud detection recall while affecting the precision-recall balance.
The trained models and preprocessing object were saved for future reuse.
