import streamlit as st

st.set_page_config(
    page_title="Hair Tracker AI",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUDOdx6MBOiP_Nx6C9JxqrUqjhSOXho-JeeQ&s",
    layout="wide",
)

from Hairfall import run_page as run_page1
from Disease import run_page as run_page2
from streamlit_option_menu import option_menu

selected=option_menu(
    menu_title="Navigation",
    options=["◖Home◗","◖HairFall Prediction◗","◖Disease Classification◗"],
    icons=["🏠","💇‍♂️","☠️"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

st.markdown("""
<style>
.wavy-text {
  font-size: 36px;
  animation: wave 3s infinite;
}

@keyframes wave {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0);
  }
}
.stAppHeader.st-emotion-cache-12fmjuu.ezrtsby2 {
  visibility: hidden;
}
.stAppToolbar.st-emotion-cache-15ecox0.ezrtsby0{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

if selected=="◖Home◗":
    st.markdown('<div class="wavy-text">Welcome User!</div>', unsafe_allow_html=True)
    content = """
    <p><strong>Overview</strong></p>
    <p>Hair Tracker AI is an innovative AI-powered application designed to address a wide range of hair-related concerns using machine learning models. The application utilizes four specialized models to deliver insights into hair loss prediction, personalized product recommendations, hair type classification, and overall hair health monitoring. By leveraging comprehensive datasets from Kaggle, the application ensures robust training and reliable predictions.</p>

    <p><strong>Key Features</strong></p>
    <ul>
    <li><strong>Hair Loss Prediction:</strong> Predicts the likelihood of hair loss by analyzing factors such as age, genetics, and lifestyle choices.</li>
    <li><strong>Hair Care Product Recommendation:</strong> Suggests optimal hair care products tailored to different hair types and conditions, offering personalized routines.</li>
    <li><strong>Hair Type Classification:</strong> Accurately identifies and classifies hair into types (straight, wavy, curly) based on visual and structural features.</li>
    <li><strong>Hair Health Monitoring:</strong> Continuously tracks hair health, identifying signs of damage or thinning for proactive care.</li>
    </ul>

    <p><strong>Datasets</strong></p>
    <ul>
    <li><strong>Hair Loss Dataset:</strong> Contains data on patterns and factors influencing hair loss.</li>
    <li><strong>Three Hair Types Dataset:</strong> Provides data for classifying hair into straight, wavy, and curly types.</li>
    <li><strong>Hair Health Dataset:</strong> Focuses on monitoring factors affecting hair health.</li>
    <li><strong>Hair Diseases Dataset:</strong> Covers various hair diseases and their symptoms for early detection and treatment recommendations.</li>
    </ul>

    <p><strong>Deployment</strong></p>
    <p>The application is developed using Streamlit, which provides a sleek and user-friendly interface. Streamlit enhances interactivity and accessibility, making it suitable for both technical and non-technical users.</p>

    <p><strong>How to Use</strong></p>
    <ul>
    <li><strong>Hair Loss Prediction:</strong> Input relevant details to receive insights on potential hair loss.</li>
    <li><strong>Product Recommendation:</strong> Get personalized suggestions for hair care products based on your specific needs.</li>
    <li><strong>Hair Type Classification:</strong> Upload a hair image or provide a description for accurate classification.</li>
    <li><strong>Hair Health Monitoring:</strong> Regularly track your hair's condition, detect issues early, and receive actionable advice.</li>
    </ul>

    <p><strong>Conclusion</strong></p>
    <p>Hair Tracker AI aims to provide a comprehensive solution for improving hair care routines and proactively addressing hair-related concerns through the power of artificial intelligence.</p>
    """
    st.markdown(content, unsafe_allow_html=True)
    post_url = 'https://twitter.com/Nightbob551/status/1842975073713750423'
    st.markdown(f'[View Tweet]({post_url})')
if selected=="◖HairFall Prediction◗":
    run_page1()
if selected=="◖Disease Classification◗":
    run_page2()

header = """
    <style>
    .header {
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        background-color: #f53b02; 
        color: #f53b02; 
        text-align: center;
        padding: 5px;
        font-size: 20px; 
        z-index: 10; 
    }
    .twitter-icon {
        position: absolute;
        top: 50%;
        right: 10px;
        transform: translateY(-50%);
        height: 20px;
        width: 20px;
    }
    .stAppHeader.st-emotion-cache-12fmjuu.ezrtsby2 {
        visibility: hidden;
    }
    .stAppToolbar.st-emotion-cache-15ecox0.ezrtsby0{
        visibility: hidden;
    }
    </style>

    <div class="header">
        <h1>◎  ᕼᗩIᖇ TᖇᗩᑕKEᖇ ᗩI  ◎</h1>
        <a href="https://x.com/Nightbob551" target="_blank">
            <img class="twitter-icon" src="https://freepnglogo.com/images/all_img/1691832581twitter-x-icon-png.png" alt="Twitter">
        </a>
    </div>
"""

st.markdown(header, unsafe_allow_html=True)
st.markdown("---")

footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color:#242323;
        color: #ede6e6;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .stAppHeader.st-emotion-cache-12fmjuu.ezrtsby2 {
        visibility: hidden;
    }
    .stAppToolbar.st-emotion-cache-15ecox0.ezrtsby0{
            visibility: hidden;
    }
    </style>

    <div class="footer">
        <p><b>∘₊✧──────✧₊∘∘₊✧──────✧₊∘     Developed by [Harshit Dhar] | &copy; 2024 All rights reserved.     ∘₊✧──────✧₊∘∘₊✧──────✧₊∘</b></p>
    </div>
    
    """

st.markdown(footer, unsafe_allow_html=True)
