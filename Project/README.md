### Project Title: Predicting Student Final Exam Scores Using Regression

#### Prepared By:
- Name: Abhishek Sahu
- Domain: Data Science
- ID : CT_CSI_DS_5981

#### Project Overview:
- This project aims to build a regression model that can predict a student’s final exam score (G3) based on various academic, demographic, and behavioral factors. Using the Student Performance dataset, we explore the impact of features like study time, past scores, absences, and family background on academic outcomes.
- By leveraging exploratory data analysis (EDA), feature engineering, model building, and advanced evaluation techniques, the goal is to uncover key factors influencing academic performance and build a model that enables early identification of students at risk—allowing timely educational support and interventions.

#### Objectives:
- Understand feature relationships through exploring data distributions, correlations, and outliers through visual EDA
- Preprocess data: handle missing values, encode categorical features, normalize where needed
- Train and evaluate regression models to predict G3 (final grade)
- Interpret model performance and feature importance using RMSE, MAE, and R² Score
- Tune models using GridSearchCV and RandomizedSearchCV for optimal performance
- Visualize results: residuals, predictions, learning curves, and error distributions
- Test robustness with multiple train-test splits
- Deployed on streamlit


#### Dataset

The dataset used for this project can be found on Kaggle:

- [Student Performance Dataset](https://www.kaggle.com/datasets/impapan/student-performance-data-set)

This dataset includes various features related to students' academic performance, such as:

- Hours studied
- Previous exam scores
- Attendance

#### Process

1. **Data Exploration**:
   - Load and examine the dataset to understand its structure and the relationships between features.
   - Visualize data distributions and correlations.

2. **Preprocessing**:
   - Handle missing values, if any.
   - Encode categorical variables.
   - Scale numerical features if necessary.

3. **Feature Engineering**:
   - Create new features that might enhance the model's performance.
   - Select relevant features based on their importance.

4. **Model Building**:
   - Use various regression techniques such as Linear Regression, Decision Tree Regression, and Random Forest Regression.
   - Train the models using the prepared dataset.

5. **Model Evaluation**:
   - Evaluate model performance using metrics like Mean Squared Error (MSE), R-squared (R²), and Root Mean Squared Error (RMSE).
   - Fine-tune models to improve accuracy.

6. **Insights and Recommendations**:
   - Analyze the results to understand which features have the most significant impact on exam scores.
   - Provide recommendations for educators based on the findings.

7.  **Deploy**:
   - Deployed the model in streamlit app
   
#### Conclusion

This project demonstrates the application of regression techniques to predict student exam scores. By leveraging the power of data and machine learning, we aim to provide educators with tools to better support their students and enhance their educational outcomes.

#### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

