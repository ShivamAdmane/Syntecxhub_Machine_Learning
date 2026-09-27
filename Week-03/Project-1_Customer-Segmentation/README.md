# Project 1 - Customer Segmentation

## Overview

This project implements customer segmentation using **K-Means clustering**.

The objective is to group customers with similar demographic, spending, and purchasing characteristics into meaningful customer segments. The project follows the Week-3 internship requirements by cleaning and scaling the data, selecting the number of clusters using the Elbow Method, applying K-Means clustering, visualizing the clusters, profiling the segments, and saving the cluster labels.

## Dataset

The project uses the provided `customer_segmentation.csv` dataset.

Original dataset:

- 2,240 customers
- 29 columns

The dataset contains customer demographic, income, spending, purchasing, and campaign-related information.

## Data Cleaning

The following preprocessing steps were performed:

- Checked dataset information and data types
- Checked missing values
- Checked duplicate rows
- Filled missing `Income` values using the median income
- Detected Income outliers using the IQR method
- Capped extreme Income values at the IQR upper bound
- Created an `Age` feature from `Year_Birth`
- Detected anomalous Age values using the IQR method
- Removed 3 clearly anomalous age records

After cleaning:

- Final number of customers: **2,237**
- Duplicate rows: **0**
- Missing Income values: **0**

## Feature Engineering

The following features were created/selected for customer segmentation:

| Feature | Description |
|---|---|
| `Age` | Customer age calculated from `Year_Birth` |
| `Income` | Customer income |
| `Total_Spending` | Total spending across product categories |
| `Total_Purchases` | Total purchases across web, catalog, and store channels |

These four features were used for clustering.

## Feature Scaling

The selected features were standardized using **StandardScaler** before applying K-Means.

Scaling was required because the features have different numerical ranges, particularly Income and Total Spending.

## Elbow Method

The Elbow Method was used to determine a suitable number of clusters.

Values of `k` from 2 to 10 were tested using K-Means inertia.

Based on the cleaned-data Elbow curve, **5 clusters** were selected.

The Elbow Method plots are saved in:

```text
outputs/elbow_method.png
outputs/elbow_method_cleaned.png






## 
K-Means Clustering

A K-Means model was trained using:

Number of clusters: 5
random_state = 42
n_init = 10

Final cluster distribution:

Cluster	Customers
0	384
1	665
2	344
3	421
4	423
Total	2,237
Customer Segment Profiles

The clusters were interpreted using Age, Income, Total Spending, and Total Purchases.

Segment	Customers	Avg. Age	Avg. Income	Avg. Spending	Avg. Purchases
High Income - High Spenders	344	36.93	75,850.93	1,453.95	20.52
Low Income - Low Spenders	665	37.07	30,821.98	83.59	5.51
Moderate Income - Moderate Spenders	384	43.22	57,046.28	604.15	15.52
Older - High Spenders	423	59.51	70,780.15	1,183.08	19.57
Older - Low Spenders	421	57.01	41,719.94	158.83	7.37
Marketing Actions
High Income - High Spenders

Characteristics:

Higher average income
Highest average spending
High purchase activity

Marketing Action:
Offer premium products, loyalty rewards, and personalized premium offers.

Low Income - Low Spenders

Characteristics:

Lowest average income
Lowest average spending
Lowest purchase activity

Marketing Action:
Use budget-friendly offers, discounts, and low-cost product recommendations.

Moderate Income - Moderate Spenders

Characteristics:

Moderate income
Moderate spending
Moderate purchase activity

Marketing Action:
Use personalized recommendations, bundle offers, and loyalty incentives.

Older - High Spenders

Characteristics:

Higher average age
Higher income
High spending and purchase activity

Marketing Action:
Promote premium products, loyalty benefits, and personalized offers suitable for mature customers.

Older - Low Spenders

Characteristics:

Higher average age
Moderate income
Lower spending and purchase activity

Marketing Action:
Use simple promotional offers, targeted discounts, and product recommendations to encourage engagement.

Cluster Visualizations

The following visualizations were created:

Income vs Total Spending
outputs/customer_clusters_income_spending.png
Age vs Total Spending
outputs/customer_clusters_age_spending.png
Customer Count by Segment
outputs/customer_segment_distribution.png

These visualizations help understand the differences between the customer segments.

Saved Outputs
Customer Segment Report
outputs/customer_segment_report.csv

This contains:

Customer count
Average age
Average income
Average spending
Average purchases
Marketing action
Customer Segmentation Results
outputs/customer_segments.csv

This contains the customer-level data along with:

Cluster
Segment
Saved Machine Learning Models

The trained K-Means model was saved as:

models/customer_segmentation_kmeans.pkl

The fitted StandardScaler was saved as:

models/customer_segmentation_scaler.pkl

The saved model and scaler were loaded successfully and tested on a customer record.


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

The Customer Segmentation project successfully groups customers into five segments using K-Means clustering.

The project includes data cleaning, feature engineering, feature scaling, Elbow Method analysis, K-Means clustering, cluster visualization, customer profiling, marketing actions, saved cluster labels, and reusable model files.