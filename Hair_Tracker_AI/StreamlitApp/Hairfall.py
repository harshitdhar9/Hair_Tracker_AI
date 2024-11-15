import streamlit as st
import joblib

def run_page():
    st.markdown(
        """
        <style>
        /* General Background and Text */
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        /* App Title */
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #007BFF;
            text-align: center;
            margin-bottom: 1em;
        }
        /* Headers */
        .section-header {
            font-size: 1.5em;
            font-weight: bold;
            color: #FF5733;
            margin-top: 1em;
        }
        /* Prediction Box */
        .prediction-box {
            background-color: #d4edda;
            border: 2px solid #28a745;
            padding: 10px;
            border-radius: 5px;
            margin-top: 1em;
            font-size: 1.2em;
            font-weight: bold;
            color: #155724;
        }
        /* Dropdown Styling */
        .stSelectbox > div {
            border: 1px solid #007BFF !important;
            border-radius: 4px;
            background-color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="main-title">Hairfall Prediction App</div>', unsafe_allow_html=True)

    model = joblib.load('Hair_Tracker_AI/StreamlitApp/XGB.joblib')

    st.markdown('<div class="section-header">Enter the Parameters</div>', unsafe_allow_html=True)

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
        if prediction == 1:
            message = "The person **might experience hairfall**."
        else:
            message = "The person **might not experience hairfall**."

        st.markdown(
            f"""
            <div class="prediction-box">
                <b>Prediction:</b> {message}
            </div>
            """,
            unsafe_allow_html=True
        )
