# Project 2 - Spam Detection

## Overview

This project implements a machine learning system for classifying email messages as **Spam** or **Ham**.

The project follows the Syntecxhub Week-2 internship requirements by loading and preprocessing a labeled spam/ham dataset, converting text into TF-IDF vectors, training a Naive Bayes classifier, evaluating the model using precision, recall and F1-score, creating a confusion matrix, and saving a reusable TF-IDF + Naive Bayes pipeline.

## Dataset

The project uses the provided `spam_ham_dataset.csv` dataset.

The original dataset contains:

- **5,171 messages**
- **3,672 Ham messages**
- **1,499 Spam messages**

The dataset contains the following columns:

- `label` - Text label indicating Ham or Spam
- `text` - Email/message content
- `label_num` - Numeric target where 0 = Ham and 1 = Spam

The `Unnamed: 0` column was removed because it was only an index column.

## Data Preprocessing

The following preprocessing steps were performed:

- Checked dataset information
- Checked missing values
- Checked class distribution
- Removed the unnecessary index column
- Checked for duplicate rows
- Removed **178 duplicate rows**
- Converted message text to lowercase
- Removed URLs
- Removed email addresses
- Removed punctuation and numbers
- Removed extra whitespace

After removing duplicates, the dataset contained:

**4,993 unique messages**

## Exploratory Data Analysis

The dataset was examined to understand the distribution of Ham and Spam messages.

After duplicate removal:

- Ham: **3,531**
- Spam: **1,462**

The dataset was divided into training and testing sets using an 80:20 split with stratification.

## Text Vectorization

The cleaned message text was converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

A maximum of 5,000 features was used and English stop words were removed.

The TF-IDF vectorizer was fitted only on the training data and then used to transform the test data.

## Machine Learning Model

### Naive Bayes

A **Multinomial Naive Bayes** classifier was trained using the TF-IDF features.

### Model Performance

| Metric | Score |
|---|---:|
| Accuracy | **95.30%** |
| Precision | **88.92%** |
| Recall | **95.90%** |
| F1 Score | **92.28%** |

### Spam Class Performance

| Metric | Score |
|---|---:|
| Precision | **88.92%** |
| Recall | **95.90%** |
| F1 Score | **92.28%** |

The high recall indicates that the model successfully detects most of the actual spam messages.

## Confusion Matrix

The confusion matrix produced the following results:

| Actual / Predicted | Ham | Spam |
|---|---:|---:|
| **Ham** | **671** | **35** |
| **Spam** | **12** | **281** |

### Interpretation

- **671 Ham** messages were correctly classified as Ham.
- **281 Spam** messages were correctly classified as Spam.
- **35 Ham** messages were incorrectly classified as Spam.
- **12 Spam** messages were incorrectly classified as Ham.

The model has high spam recall, meaning it catches most actual spam messages. There are fewer false negatives than false positives.

The confusion matrix is saved as:

```text
outputs/confusion_matrix_naive_bayes.png






###
Reusable Machine Learning Pipeline

A complete TF-IDF + Naive Bayes Pipeline was created using Scikit-learn.

The pipeline combines:

TF-IDF text vectorization
Multinomial Naive Bayes classification

This allows new messages to be passed directly to the saved pipeline without manually performing the vectorization steps.

The saved pipeline is:

models/spam_detection_tfidf_naive_bayes_pipeline.pkl
Testing with New Messages

The saved pipeline was tested with new messages.

Example spam message:

Congratulations! You have won a free prize. Click the link to claim your reward now.

Prediction:

Spam

Example normal message:

Hi, please send me the project report when you get time.

Prediction:

Ham
Project Outputs

The following visualizations were created:

outputs/
├── confusion_matrix_naive_bayes.png
└── spam_detection_metrics.png
Project Structure
Project-2_Spam-Detection
│
├── data
│   └── spam_ham_dataset.csv
│
├── models
│   └── spam_detection_tfidf_naive_bayes_pipeline.pkl
│
├── notebooks
│   └── spam_detection.ipynb
│
├── outputs
│   ├── confusion_matrix_naive_bayes.png
│   └── spam_detection_metrics.png
│
├── src
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

The Spam Detection project successfully demonstrates text preprocessing, TF-IDF feature extraction and Naive Bayes classification.

The model achieved 95.30% accuracy, with a 95.90% recall and 92.28% F1-score for the overall evaluation.

A reusable TF-IDF + Naive Bayes pipeline was also saved and successfully tested on new messages.


This README follows the Week-2 Project 2 requirements from the internship document: preprocessing, TF-IDF/CountVectorizer, Naive Bayes or Logistic Regression, precision/recall/F1 evaluation, and saving the reusable vectorizer/model pipeline. :contentReference[oaicite:0]{index=0}

Press **Ctrl + S** after pasting.

Tell me **Done** once the README is saved.