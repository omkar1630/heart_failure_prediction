# ❤️ Heart Failure Prediction using Logistic Regression

A Machine Learning web application built with Streamlit that predicts the risk of heart failure based on patient health parameters.

## 🚀 Live Demo

🌐 Live App: https://fraud-detection-project-1-8kj4.onrender.com/

---

## 📌 Project Overview

This project uses a Logistic Regression model to predict whether a patient is at risk of heart failure. Users can enter medical details through an interactive Streamlit interface and instantly receive a prediction.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-Learn
- NumPy
- Pickle

---

## 📊 Features

- Attractive and responsive UI
- Real-time prediction
- User-friendly dropdowns and inputs
- Displays prediction as categorical output
- Shows prediction confidence score
- Easy deployment on Render

---

## 📋 Input Features

| Feature | Description |
|----------|-------------|
| Age | Patient Age |
| Anaemia | Whether patient has anaemia |
| Creatinine Phosphokinase | CPK enzyme level |
| Diabetes | Whether patient has diabetes |
| Ejection Fraction | Percentage of blood leaving heart |
| High Blood Pressure | Presence of hypertension |
| Platelets | Platelet count |
| Serum Creatinine | Creatinine level in blood |
| Serum Sodium | Sodium level in blood |
| Gender | Male/Female |
| Smoking | Smoking habit |
| Follow-up Time | Follow-up period |

---

## 🎯 Prediction Output

The model predicts:

- ✅ No Heart Failure Risk
- ⚠️ Heart Failure Risk Detected

---

## 📂 Project Structure

```text
Heart-Failure-Prediction/
│
├── app.py
├── logistic.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/heart-failure-prediction.git
```

Move into project folder:

```bash
cd heart-failure-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🚀 Deployment on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 📈 Machine Learning Model

Algorithm Used:

- Logistic Regression

Model File:

- logistic.pkl

---

## 👨‍💻 Author

**Omkar Raut**

- GitHub: https://github.com/your-github-username
- LinkedIn: https://linkedin.com/in/your-linkedin-profile

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
