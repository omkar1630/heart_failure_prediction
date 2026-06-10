import streamlit as st
import pickle
import numpy as np

# Page Config
st.set_page_config(
    page_title="Heart Failure Prediction",
    page_icon="❤️",
    layout="wide"
)

# Load Model
with open("logistic.pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align:center;
    color:#ff4b4b;
    font-size:42px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}
.stButton>button{
    width:100%;
    background-color:#ff4b4b;
    color:white;
    font-size:18px;
    border-radius:10px;
}
.result{
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">❤️ Heart Failure Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict the risk of heart failure using Machine Learning</p>', unsafe_allow_html=True)

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120, 50)
    anaemia = st.selectbox("Anaemia", [0, 1])
    creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", 0, 10000, 500)
    diabetes = st.selectbox("Diabetes", [0, 1])

with col2:
    ejection_fraction = st.number_input("Ejection Fraction", 1, 100, 35)
    high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1])
    platelets = st.number_input("Platelets", 0.0, 1000000.0, 250000.0)
    serum_creatinine = st.number_input("Serum Creatinine", 0.0, 20.0, 1.0)

with col3:
    serum_sodium = st.number_input("Serum Sodium", 100, 200, 137)
    sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
    smoking = st.selectbox("Smoking", [0, 1])
    time = st.number_input("Follow-up Time", 0, 500, 100)

if st.button("🔍 Predict"):
    
    features = np.array([[
        age,
        anaemia,
        creatinine_phosphokinase,
        diabetes,
        ejection_fraction,
        high_blood_pressure,
        platelets,
        serum_creatinine,
        serum_sodium,
        sex,
        smoking,
        time
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    st.write("")

    if prediction == 1:
        st.error(
            f"⚠️ High Risk of Heart Failure\n\nProbability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Low Risk of Heart Failure\n\nProbability: {probability:.2%}"
        )

st.write("---")
st.caption("Built with Streamlit & Logistic Regression")
