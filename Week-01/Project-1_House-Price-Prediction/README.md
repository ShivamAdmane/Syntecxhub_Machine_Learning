# House Price Prediction

## Project Overview

This project was completed as part of the Syntecxhub Machine Learning Internship.

The objective of this project is to build a Linear Regression model that predicts median house values using housing-related features.

## Dataset

The project uses the California Housing dataset.

The dataset contains housing-related features such as:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

The target variable is `MedHouseVal`, representing the median house value.

## Project Workflow

The project follows these steps:

1. Load the housing dataset
2. Understand the dataset
3. Check for missing values
4. Check for duplicate records
5. Perform exploratory data analysis
6. Analyze feature correlations
7. Select input features and target variable
8. Split the dataset into training and testing sets
9. Train a Linear Regression model
10. Generate predictions
11. Evaluate the model using RMSE and R²
12. Interpret model coefficients
13. Save the trained model
14. Load the saved model and verify predictions

## Model

### Linear Regression

The model uses the following features:

- `MedInc`
- `HouseAge`
- `AveRooms`
- `AveBedrms`
- `Population`
- `AveOccup`
- `Latitude`
- `Longitude`

Target:

- `MedHouseVal`

## Model Evaluation

The model achieved:

- **RMSE:** 0.7455
- **R² Score:** 0.5758

The R² score indicates that the model explains approximately 57.58% of the variation in the target variable.

## Project Structure

```text
Project-1_House-Price-Prediction
│
├── data
│   └── housing.csv
│
├── notebooks
│   └── house_price_prediction.ipynb
│
├── models
│   └── linear_regression_house_price_model.pkl
│
├── outputs
├── src
├── README.md
└── requirements.txt