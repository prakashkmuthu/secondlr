import streamlit as st
import requests

st.title("Salary Prediction App")

experience = st.number_input("Enter years of experience", min_value=0.0, step=1.0)

if st.button("Predict Salary"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"experience": experience}
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Salary: ₹{result['prediction']:.2f}")
    else:
        st.error("Something went wrong. Please check FastAPI server.")