# Project 2 - Salary Prediction

## Overview

This project demonstrates Linear Regression using the provided Ecommerce Customers dataset.

The objective is to predict the **Yearly Amount Spent** by a customer based on customer engagement and membership-related features.

The project follows a Linear Regression workflow including data inspection, preprocessing, feature selection, model training, evaluation, model comparison, visualization, and model saving.

> **Note:** The internship task is titled "Salary Prediction", while the provided dataset contains Ecommerce Customer data with `Yearly Amount Spent` as the target variable. Therefore, this implementation uses the provided dataset and predicts Yearly Amount Spent.

## Dataset

The dataset used in this project is:

**Ecommerce Customers**

It contains 500 customer records and the following columns:

- Email
- Address
- Avatar
- Avg. Session Length
- Time on App
- Time on Website
- Length of Membership
- Yearly Amount Spent

### Target Variable

`Yearly Amount Spent`

### Selected Features

The following numerical features were selected for prediction:

- Avg. Session Length
- Time on App
- Time on Website
- Length of Membership

Email, Address, and Avatar were not used as predictive features.

## Project Workflow

1. Load the dataset
2. Inspect the dataset using `info()` and `describe()`
3. Check for missing values
4. Check for duplicate records
5. Select features and target variable
6. Split the data into training and testing sets
7. Train a Single-Feature Linear Regression model
8. Train a Multiple Linear Regression model
9. Evaluate models using RMSE and R² Score
10. Compare both models
11. Analyze feature coefficients
12. Visualize feature coefficients
13. Visualize actual vs predicted values
14. Save the best-performing model
15. Generate example predictions

## Models

### 1. Single-Feature Linear Regression

The first model uses only:

`Time on App`

Results:

- RMSE: **64.2130**
- R² Score: **0.1673**

### 2. Multiple Linear Regression

The second model uses all four selected features:

- Avg. Session Length
- Time on App
- Time on Website
- Length of Membership

Results:

- RMSE: **10.4816**
- R² Score: **0.9778**

### Model Comparison

| Model | RMSE | R² Score |
|---|---:|---:|
| Single Feature (Time on App) | 64.2130 | 0.1673 |
| Multiple Features (All 4) | 10.4816 | 0.9778 |

The Multiple Linear Regression model performs significantly better, with a much lower RMSE and a much higher R² Score.

## Feature Coefficients

The coefficients obtained from the Multiple Linear Regression model are:

| Feature | Coefficient |
|---|---:|
| Length of Membership | 61.8968 |
| Time on App | 38.7853 |
| Avg. Session Length | 25.5963 |
| Time on Website | 0.3104 |

All four coefficients are positive, indicating a positive relationship with Yearly Amount Spent when the other features are held constant.

`Length of Membership` has the largest coefficient among the selected features.

## Example Predictions

The trained Multiple Linear Regression model was used to generate example predictions on the test dataset.

The predictions were compared with the actual Yearly Amount Spent values to evaluate how closely the model performs on unseen data.

## Saved Model

The best-performing Multiple Linear Regression model is saved as:

```text
models/multiple_linear_regression_model.pkl


### 
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Jupyter Notebook
Evaluation Metrics
RMSE

Root Mean Squared Error (RMSE) measures the average magnitude of prediction errors. Lower RMSE indicates better model performance.

R² Score

R² Score measures how well the model explains the variation in the target variable. A value closer to 1 indicates better explanatory performance.

Conclusion

The Multiple Linear Regression model performed considerably better than the Single-Feature Linear Regression model.

Using all four selected features resulted in an RMSE of 10.4816 and an R² Score of 0.9778.

Therefore, the Multiple Linear Regression model was selected as the best model and saved for future predictions.