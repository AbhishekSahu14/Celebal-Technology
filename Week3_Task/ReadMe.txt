Title: Exploratory Data Visualization on Breast Cancer Diagnosis Dataset

Prepared by:
- Name: ABHISHEK SAHU
- Mail: sahuabhishek142004@gmail.com

Project Overview:
This project focuses on performing data visualization using the Breast Cancer Wisconsin dataset. The dataset contains medical measurements of tumors, and the objective is to uncover patterns, trends, and insights that differentiate malignant (M) and benign (B) tumors.

Using a variety of visual techniques, we aim to better understand the distribution of features, relationships between variables, and the characteristics associated with cancer diagnosis. These visual insights can guide future modeling efforts and aid in building interpretable, data-driven decision systems for early detection.

Key Objectives:
- Analyze the distribution of features for malignant vs. benign tumors.
- Visualize correlations between features.
- Identify the most distinguishing attributes using plots.
- Summarize patterns and insights that can inform predictive modeling.

Dataset Metadata:

Property                | Value
------------------------|--------------------------------------------------------------
Dataset Name            | Breast Cancer Wisconsin (Diagnostic) Dataset
Source                  | UCI Machine Learning Repository / Kaggle
File Name               | breastcancer.csv
Number of Instances     | 569
Number of Features      | 32 (including ID and target; 30 numeric predictors)
Target Variable         | diagnosis
Classes                 | M = Malignant (cancerous), B = Benign (non-cancerous)
Missing Values          | Unnamed: 32 column is entirely NaN; other columns are clean
Feature Types           | All features (except id, diagnosis) are numeric (float)

Feature Groups:

Group               | Features
-------------------|------------------------------------------------------------
Mean Values         | *_mean: radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, fractal dimension
Standard Errors     | *_se: same properties, standard error
Worst Values        | *_worst: largest value for the same properties
