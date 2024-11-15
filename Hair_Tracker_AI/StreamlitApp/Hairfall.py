import streamlit as st
import joblib

model = joblib.load('hairfall_model.joblib')

st.title("Hairfall Prediction App")

st.header("Enter the Parameters")

pressure_options = [0, 1, 2, 3]
stress_options = [0, 1, 2, 3]
hair_grease_options = [3.0, 1.0, 2.0, 4.0, 5.0]
dandruff_options = [1.0, 2.0]

pressure_level = st.selectbox("Pressure Level", pressure_options)
stress_level = st.selectbox("Stress Level", stress_options)
hair_grease = st.selectbox("Hair Grease Level", hair_grease_options)
dandruff = st.selectbox("Dandruff Level", dandruff_options)

if st.button("Predict"):
    inputs = [[pressure_level, stress_level, hair_grease, dandruff]]
    prediction = model.predict(inputs)[0]
    st.subheader("Prediction")
    st.write(f"The predicted hairfall level is: {prediction}")
