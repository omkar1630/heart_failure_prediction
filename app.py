import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Heart Failure Prediction",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
with open("logistic.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

.title {
    text-align: center;
    color: #e63946;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    background-color: #e63946;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
}

.stButton > button:hover {
    background-color: #c1121f;
    color: white;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="title">❤️ Heart Failure Prediction</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict Heart Failure Risk using Machine Learning</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Input Fields
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=60)
    anaemia = st.selectbox("Anaemia", ["No", "Yes"])
    creatinine_phosphokinase = st.number_input(
        "Creatinine Phosphokinase",
        min_value=0,
        value=500
    )
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])

with col2:
    ejection_fraction = st.number_input(
        "Ejection Fraction",
        min_value=1,
        max_value=100,
        value=38
    )
    high_blood_pressure = st.selectbox(
        "High Blood Pressure",
        ["No", "Yes"]
    )
    platelets = st.number_input(
        "Platelets",
        min_value=0.0,
        value=263358.0
    )
    serum_creatinine = st.number_input(
        "Serum Creatinine",
        min_value=0.0,
        value=1.1
    )

with col3:
    serum_sodium = st.number_input(
        "Serum Sodium",
        min_value=100,
        max_value=200,
        value=136
    )
    sex = st.selectbox("Gender", ["Female", "Male"])
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    time = st.number_input(
        "Follow-up Time",
        min_value=0,
        value=120
    )

# Convert categorical values
anaemia = 1 if anaemia == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0
high_blood_pressure = 1 if high_blood_pressure == "Yes" else 0
smoking = 1 if smoking == "Yes" else 0
sex = 1 if sex == "Male" else 0

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Heart Failure Risk"):

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

    try:
        probability = model.predict_proba(features)[0][1]
    except:
        probability = None

    st.markdown("---")

    if prediction == 1:
        st.error("⚠️ Heart Failure Risk Detected")

        if probability is not None:
            st.metric(
                label="Risk Probability",
                value=f"{probability:.2%}"
            )

    else:
        st.success("✅ No Heart Failure Risk")

        if probability is not None:
            st.metric(
                label="Confidence",
                value=f"{(1-probability):.2%}"
            )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    '<div class="footer">Built with Streamlit & Logistic Regression ❤️</div>',
    unsafe_allow_html=True
)
