
COVID-19 Patient Data – Exploratory Data Analysis (EDA)

Task Overview:
This project aims to perform a comprehensive Exploratory Data Analysis (EDA) on a large-scale COVID-19 patient dataset. The dataset includes over 1 million patient records with clinical and demographic features.
The raw dataset consists of 21 unique features and 1,048,576 unique patients. The goal is to uncover insights into patient outcomes, comorbidities, treatment types, and mortality risk factors.

DatasetLink - 

Objectives:
- Understand the distribution of patient characteristics (age, sex, medical unit, comorbidities).
- Analyze mortality trends based on age, sex, ICU admission, and underlying health conditions.
- Explore the relationships between intubation, ICU admission, and patient outcomes.
- Identify correlations among features to find potential predictors of severe COVID-19 cases.
- Detect and visualize missing values, outliers, and data imbalances.

Key Dataset Features:
- Demographic: SEX, AGE, PREGNANT
- Comorbidities: DIABETES, COPD, ASTHMA, OBESITY, etc.
- Outcomes: DATE_DIED, ICU, INTUBED, CLASIFFICATION_FINAL
- Treatment context: USMER, MEDICAL_UNIT, PATIENT_TYPE

Tools Used:
- Numpy, Pandas, Seaborn, Matplotlib
- Visualizations: heatmaps, count plots, box plots, violin plots, etc.

Outcomes:
- Cleaned and processed dataset
- Visual dashboards summarizing key insights
- EDA report or Jupyter notebook with detailed commentary
