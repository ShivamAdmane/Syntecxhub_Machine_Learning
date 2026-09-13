# Project 1 - Flower Classification

## Overview

This project implements a machine learning classification system for identifying Iris flower species from their sepal and petal measurements.

The project follows the Syntecxhub Week-2 internship requirements by performing Exploratory Data Analysis (EDA), visualizing feature pairs, training Logistic Regression and Decision Tree classifiers, comparing their accuracy, analyzing confusion matrices, and building a command-line prediction script.

## Dataset

The project uses the **Iris dataset**.

The dataset contains 150 flower samples with four numerical features:

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

There are three target classes:

- Setosa
- Versicolor
- Virginica

Each species contains 50 samples.

## Exploratory Data Analysis

The dataset was inspected using:

- Dataset shape and information
- Statistical summary
- Missing-value analysis
- Species distribution
- Feature-pair visualization

### Dataset Information

- Total samples: **150**
- Features: **4**
- Target classes: **3**
- Missing values: **0**
- Samples per class: **50**

### Feature Pair Visualization

A Seaborn pair plot was created to visualize relationships between the four flower measurements.

The visualization shows that Setosa is clearly separated from the other species, while Versicolor and Virginica have some overlap.

The feature-pair visualization is saved as:

```text
outputs/feature_pair_plot.png





###
Machine Learning Models

Two classification algorithms were trained:

1. Logistic Regression

Accuracy:

96.67%

2. Decision Tree

Accuracy:

93.33%

Model Comparison
Classifier	Accuracy
Logistic Regression	96.67%
Decision Tree	93.33%

For the selected train-test split, Logistic Regression achieved the higher accuracy.

The accuracy comparison is saved as:

outputs/model_accuracy_comparison.png
Confusion Matrix and Misclassification Analysis

Confusion matrices were created separately for both classifiers.

Saved files:

outputs/confusion_matrix_logistic_regression.png
outputs/confusion_matrix_decision_tree.png
Misclassifications

The models mainly had difficulty distinguishing between Versicolor and Virginica.

Observed misclassified test samples:

Actual Species	Logistic Regression	Decision Tree
Virginica	Virginica	Versicolor
Versicolor	Virginica	Virginica

Logistic Regression made one misclassification, while Decision Tree made two misclassifications on the test set.

Setosa was classified correctly.

The overlap between Versicolor and Virginica observed in the feature-pair visualization helps explain why these classes are more difficult to distinguish.

Flower Prediction CLI

A command-line prediction script was created to predict the species of a new flower using four measurements:

Sepal Length
Sepal Width
Petal Length
Petal Width

The script is located at:

src/predict_flower.py

Example command:

py -3.14 Week-02/Project-1_Flower-Classification/src/predict_flower.py --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2

Example output:

Predicted Flower Species: setosa
Saved Models

Both trained models were saved using Joblib:

models/
├── logistic_regression_iris_model.pkl
└── decision_tree_iris_model.pkl
Project Structure
Project-1_Flower-Classification
│
├── data
│
├── models
│   ├── logistic_regression_iris_model.pkl
│   └── decision_tree_iris_model.pkl
│
├── notebooks
│   └── flower_classification.ipynb
│
├── outputs
│   ├── feature_pair_plot.png
│   ├── confusion_matrix_logistic_regression.png
│   ├── confusion_matrix_decision_tree.png
│   └── model_accuracy_comparison.png
│
├── src
│   └── predict_flower.py
│
├── README.md
└── requirements.txt
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Jupyter Notebook
Conclusion

The Iris flower classification project successfully demonstrates the use of Logistic Regression and Decision Tree classifiers.

Logistic Regression achieved 96.67% accuracy, while the Decision Tree achieved 93.33% accuracy on the test set.

Therefore, Logistic Regression performed better for this particular train-test split and was also used for the command-line flower prediction script.