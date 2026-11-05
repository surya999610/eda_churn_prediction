import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Telecom Customer Churn Predictor",
    page_icon="📞",
    layout="wide"
)

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load('random_forest_churn_model.pkl')

model = load_model()

# Title and Description
st.title("📞 Telecom Customer Churn Prediction App")
st.write("Enter the customer details below to predict the likelihood of churn.")

st.markdown("---")

# Layout inputs with Markdown Range Guides
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Demographics & Account Info")
    
    telecom_partner = st.selectbox("Telecom Partner", ["Reliance Jio", "Vodafone", "Airtel", "BSNL"])
    st.markdown("*Select one of the available network providers.*")
    
    gender = st.selectbox("Gender", ["F", "M"])
    st.markdown("*Select gender: **F** (Female) or **M** (Male).*")
    
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    st.markdown("*Allowed range: **18** to **100** years.*")
    
    num_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=1)
    st.markdown("*Allowed range: **0** to **10** family members.*")

with col2:
    st.subheader("Location & Dates")
    
    state = st.selectbox("State", ["Karnataka", "Mizoram", "Arunachal Pradesh", "Tamil Nadu", "Tripura", "Assam", "Madhya Pradesh", "Telangana", "Uttarakhand", "Other"])
    st.markdown("*Select customer's state of residence.*")
    
    city = st.selectbox("City", ["Kolkata", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Other"])
    st.markdown("*Select customer's city of residence.*")
    
    estimated_salary = st.number_input("Estimated Salary (₹)", min_value=10000, max_value=500000, value=85000)
    st.markdown("*Allowed range: **₹10,000** to **₹5,00,000**.*")
    
    reg_date = st.date_input("Registration Date", datetime(2022, 1, 1))
    st.markdown("*Select date when customer account was registered.*")

with col3:
    st.subheader("Usage Metrics")
    
    calls_made = st.number_input("Calls Made", min_value=0, max_value=500, value=50)
    st.markdown("*Allowed range: **0** to **500** calls.*")
    
    sms_sent = st.number_input("SMS Sent", min_value=0, max_value=200, value=20)
    st.markdown("*Allowed range: **0** to **200** messages.*")
    
    data_used = st.number_input("Data Used (MB)", min_value=0, max_value=50000, value=4000)
    st.markdown("*Allowed range: **0** to **50,000** MB (50 GB).*")

st.markdown("---")

# Dictionary encodings
partner_map = {"Airtel": 0, "BSNL": 1, "Reliance Jio": 2, "Vodafone": 3}
gender_map = {"F": 0, "M": 1}

# Function to calculate age_group
def get_age_group(age_val):
    if age_val < 25:
        return 0  # Young
    elif age_val < 45:
        return 1  # Adult
    elif age_val < 60:
        return 2  # Middle-aged
    else:
        return 3  # Senior

# Predict Button
if st.button("Predict Churn Status", use_container_width=True):
    # Derive required engineered features
    age_group_val = get_age_group(age)
    reg_month = reg_date.month
    reg_year = reg_date.year

    # Construct dataframe matching exact training columns
    input_data = pd.DataFrame([{
        'telecom_partner': partner_map.get(telecom_partner, 0),
        'gender': gender_map.get(gender, 0),
        'age': age,
        'num_dependents': num_dependents,
        'estimated_salary': estimated_salary,
        'calls_made': calls_made,
        'sms_sent': sms_sent,
        'data_used': data_used,
        'age_group': age_group_val,
        'registration_month': reg_month,
        'registration_year': reg_year
    }])

    # Reorder columns automatically to match model's expected order
    if hasattr(model, 'feature_names_in_'):
        input_data = input_data[list(model.feature_names_in_)]

    # Generate predictions
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1] * 100

    # Display output
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ **High Risk of Churn!** (Probability: {prediction_proba:.2f}%)")
    else:
        st.success(f"✅ **Low Risk of Churn.** (Probability of Churn: {prediction_proba:.2f}%)") 
         