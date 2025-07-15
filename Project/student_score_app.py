import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ------------------------------
# Load artifacts
# ------------------------------
model = joblib.load('best_random_forest_model.pkl')
onehot_encoder = joblib.load('onehot_encoder.pkl')
scaler = joblib.load('scaler.pkl')
onehot_cols = joblib.load('onehot_cols.pkl')
dummy_cols = joblib.load('dummy_cols.pkl')
numerical_cols = joblib.load('numerical_cols.pkl')
label_mappings = joblib.load('label_mappings.pkl')

st.title("🎓 Student Final Exam Score Prediction")

st.markdown(
    """
    This app predicts a student's final exam score (G3) based on their demographic, academic,
    and lifestyle features. Please fill in the details below 👇
    """
)

# -------------------------------------
# User Inputs (matching your trained classes!)
# -------------------------------------

# Build selectboxes for all categorical inputs using label mappings
sex = st.selectbox('Sex', list(label_mappings['sex'].keys()))
address = st.selectbox('Address Type', list(label_mappings['address'].keys()))
Pstatus = st.selectbox('Parent Cohabitation Status', list(label_mappings['Pstatus'].keys()))

age = st.slider('Age', 15, 22, 17)
Medu = st.selectbox('Mother\'s Education (0=none to 4=high)', [0, 1, 2, 3, 4])
Fedu = st.selectbox('Father\'s Education (0=none to 4=high)', [0, 1, 2, 3, 4])
traveltime = st.slider('Travel Time (1=low to 4=high)', 1, 4, 1)
studytime = st.slider('Study Time (1=low to 4=high)', 1, 4, 2)
failures = st.slider('Past Class Failures', 0, 3, 0)
famrel = st.slider('Family Relationship Quality (1=very bad to 5=excellent)', 1, 5, 4)
freetime = st.slider('Free Time After School (1=very low to 5=very high)', 1, 5, 3)
goout = st.slider('Going Out with Friends (1=low to 5=high)', 1, 5, 3)
Dalc = st.slider('Workday Alcohol Consumption (1=very low to 5=very high)', 1, 5, 1)
Walc = st.slider('Weekend Alcohol Consumption (1=very low to 5=very high)', 1, 5, 2)
health = st.slider('Health Status (1=very bad to 5=very good)', 1, 5, 3)
absences = st.number_input('Number of School Absences', 0, 100, 4)

# Binary yes/no options
binary_options = {}
for col in ['schoolsup', 'famsup', 'paid', 'activities', 'higher', 'internet', 'romantic']:
    binary_options[col] = st.selectbox(col.replace('_', ' ').title(), list(label_mappings[col].keys()))

# Mjob and Fjob (same way as training)
mjob = st.selectbox('Mother\'s Job', ['at_home', 'health', 'other', 'services', 'teacher'])
fjob = st.selectbox('Father\'s Job', ['at_home', 'health', 'other', 'services', 'teacher'])

# -------------------------------------
# Build the input DataFrame
# -------------------------------------
user_data = pd.DataFrame({
    'sex': [sex],
    'age': [age],
    'address': [address],
    'Pstatus': [Pstatus],
    'Medu': [Medu],
    'Fedu': [Fedu],
    'traveltime': [traveltime],
    'studytime': [studytime],
    'failures': [failures],
    'famrel': [famrel],
    'freetime': [freetime],
    'goout': [goout],
    'Dalc': [Dalc],
    'Walc': [Walc],
    'health': [health],
    'absences': [absences],
    'Mjob': [mjob],
    'Fjob': [fjob]
})

for col, val in binary_options.items():
    user_data[col] = [val]

# Derived features
user_data['ParentEdu'] = user_data['Medu'] + user_data['Fedu']
user_data['log_absences'] = np.log1p(user_data['absences'])
user_data['HighFamRel'] = (user_data['famrel'] >= 4).astype(int)

# -------------------------------------
# Label Encoding for OneHotCols
# -------------------------------------
for col in onehot_cols:
    mapping = label_mappings[col]
    user_data[col] = user_data[col].map(mapping)
    user_data[col] = user_data[col].fillna(0).astype(int)

# -------------------------------------
# OneHot Encoding
# -------------------------------------
user_encoded = onehot_encoder.transform(user_data[onehot_cols])
user_encoded_df = pd.DataFrame(
    user_encoded,
    columns=onehot_encoder.get_feature_names_out(onehot_cols)
)
user_data = user_data.drop(columns=onehot_cols)
user_data = pd.concat([user_data.reset_index(drop=True), user_encoded_df.reset_index(drop=True)], axis=1)

# -------------------------------------
# Get dummies for Mjob and Fjob
# -------------------------------------
user_data = pd.get_dummies(user_data, columns=dummy_cols, drop_first=True)

# -------------------------------------
# Ensure all model features
# -------------------------------------
for col in model.feature_names_in_:
    if col not in user_data.columns:
        user_data[col] = 0
user_data = user_data[model.feature_names_in_]

# -------------------------------------
# Scale numerical
# -------------------------------------
#user_data[numerical_cols] = scaler.transform(user_data[numerical_cols])
final_feature_list = joblib.load('trained_columns.pkl')

for col in final_feature_list:
    if col not in user_data.columns:
        user_data[col] = 0
user_data = user_data[final_feature_list]

# -------------------------------------
# Predict
# -------------------------------------
if st.button('Predict Final Exam Score'):
    prediction = model.predict(user_data)[0]
    st.success(f"🎯 Predicted Final Exam Score (log scale): {prediction:.2f}")
    score_exp = np.expm1(prediction)
    st.success(f"✅ Approximate Predicted Final Exam Score: {score_exp:.0f}")
