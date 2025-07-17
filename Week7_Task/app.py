import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ------------------------------
# Load trained model & scaler
# ------------------------------
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# ------------------------------
# App UI
# ------------------------------
st.set_page_config(page_title="Diabetes Prediction App", layout="centered")
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below to check the likelihood of diabetes.")

# ------------------------------
# Input Fields
# ------------------------------
st.header("🔢 Patient Information")
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20)
glucose = st.number_input("Glucose Level", min_value=0, max_value=200)
bp = st.number_input("Blood Pressure", min_value=0, max_value=150)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100)
insulin = st.number_input("Insulin", min_value=0, max_value=900)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, format="%.2f")
age = st.number_input("Age", min_value=1, max_value=120)

# ------------------------------
# Prediction Logic
# ------------------------------
if st.button("🧪 Predict"):
    input_data = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.subheader("🔍 Prediction Result:")
    if prediction == 1:
        st.error("Prediction: Diabetic")
    else:
        st.success("Prediction: Not Diabetic")

# ------------------------------
# Optional: Model Comparison Table
# ------------------------------
st.markdown("---")
st.subheader("📊 Model Comparison Table")

model_table = pd.DataFrame({
    'Model': [
        'Logistic Regression',
        'KNN Classifier',
        'Decision Tree Classifier',
        'Random Forest Classifier',
        'SVM Classifier',
        'Naive Bayes Classifier'
    ],
    'Accuracy Score': [0.818182, 0.779221, 0.818182, 0.805195, 0.798701, 0.792208]
})

st.dataframe(model_table.sort_values(by='Accuracy Score', ascending=False), use_container_width=True)
