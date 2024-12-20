import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time
import joblib
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray,rgba2rgb
from skimage import io
from io import BytesIO
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("Hair_Tracker_AI/StreamlitApp/hair_disease_cnn_model (1).h5")
model1=tf.keras.models.load_model("Hair_Tracker_AI/StreamlitApp/hair_type_classifier.h5")

import os
h5_model_path = 'Hair_Tracker_AI/StreamlitApp/hair_disease_cnn_model (1).h5'
if not os.path.exists(h5_model_path):
    print(f"Error: {h5_model_path} not found!")
else:
    print(f"Found: {h5_model_path}")
pkl_model_path = 'Hair_Tracker_AI/StreamlitApp/hair_type_classifier.h5'
if not os.path.exists(pkl_model_path):
    print(f"Error: {pkl_model_path} not found!")
else:
    print(f"Found: {pkl_model_path}")

st.markdown("""
    <style>
    .image-uploader h3 {
        font-size: 24px;
        color: #2c3e50;
        font-weight: bold;
        text-align: left;
        padding-bottom: 10px;
    }
    .uploaded-image {
        border: 2px solid #2c3e50;
        border-radius: 10px;
        padding: 5px;
    }
    .file-uploader {
        margin-top: 20px;
        padding: 10px;
        background-color: #f8f9fa;
        border: 2px solid #3498db;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def preprocess_image(img):
    img = img.resize((150, 150))  
    img = np.array(img) / 255.0  
    img = np.expand_dims(img, axis=0)  
    return img
    
def preprocess_image1(img):
    img = img.resize((150, 150)) 
    img_array = np.array(img) 
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  
    return img_array
    
def run_page():
    st.markdown('<div class="image-uploader"><h3>Upload the image of area affected by hair disease</h3></div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label="Choose a jpeg, jpg file", type=('jpg', 'jpeg'), key='file-upload1', help='Upload a .jpg or .jpeg image')
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        small_img = image.resize((300, 300))
        st.image(small_img, caption="Uploaded Image.",width=300)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        class_idx = np.argmax(prediction, axis=1)[0]
        diseases = [
        "Alopecia Areata",
        "Contact Dermatitis",
        "Folliculitis",
        "Head Lice",
        "Lichen Planus",
        "Male Pattern Baldness",
        "Psoriasis",
        "Seborrheic Dermatitis",
        "Telogen Effluvium",
        "Tinea Capitis"
    ]
        disease = diseases[class_idx] 
    
        st.markdown(
            f"""
            <style>
            .prediction-box {{
                font-size: 24px;
                color: #FF4500;
                font-weight: bold;
                text-align: center;
                border: 2px solid #FF4500;
                padding: 20px;
                margin-top: 20px;
                border-radius: 10px;
                animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
                white-space: nowrap;
                overflow: hidden;
                width: 100%;
            }}
    
            @keyframes typing {{
                from {{ width: 0; }}
                to {{ width: 100%; }}
            }}
        
            @keyframes blink-caret {{
                from, to {{ border-color: transparent; }}
                50% {{ border-color: orange; }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(f'<div class="prediction-box">Prediction: {disease}</div>', unsafe_allow_html=True)
            
    st.markdown('<div class="image-uploader"><h3>Upload the image of your hair to get hair type</h3></div>', unsafe_allow_html=True)
    uploaded_file1 = st.file_uploader(label="Choose a jpeg, jpg file", type=('jpg', 'jpeg'), key='file-upload2', help='Upload a .jpg or .jpeg image')
    categories = ['Curly Hair', 'Straight Hair', 'Wavy Hair']
    target_size = (15, 15)
    if uploaded_file1:
        try:
            img = Image.open(uploaded_file1)
            st.image(img, caption='Uploaded Image',width=300)
    
            img_array = preprocess_image1(img)
            prediction = model1.predict(img_array)
            class_names = ['Curly Hair', 'Straight Hair', 'Wavy Hair'] 
            predicted_class = class_names[np.argmax(prediction)]
            st.markdown(
            f'<div class="prediction-box">Hair Type Prediction: {predicted_class}</div>',
            unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error processing the image: {e}")
            
    import pandas as pd
    data = {
        "Disease Name": [
            "Alopecia Areata",
            "Contact Dermatitis",
            "Folliculitis",
            "Head Lice",
            "Lichen Planus",
            "Male Pattern Baldness",
            "Psoriasis",
            "Seborrheic Dermatitis",
            "Telogen Effluvium",
            "Tinea Capitis"

        ],
        "Treatment 1": [
            "Corticosteroids (topical, intralesional, or systemic)",
            "Topical corticosteroids",
            "Warm compresses",
            "Over-the-counter lice medications (e.g., permethrin, benzyl benzoate)",
            "Topical corticosteroids",
            "Minoxidil",
            "Topical corticosteroids",
            "Topical antifungal medications (e.g., ketoconazole)",
            "Observation (often resolves on its own)",
            "Oral antifungal medications (e.g., griseofulvin, terbinafine)"
        ],
        "Treatment 2": [
            "Minoxidil",
            "Antihistamines",
            "Topical antibiotics",
            "Fine-toothed comb",
            "Antimalarial drugs",
            "Finasteride",
            "Light therapy (e.g., UVB, narrowband UVB)",
            "Topical corticosteroids",
            "Iron supplements (if iron-deficient)",
            "Topical antifungal shampoo"
        ],
        "Treatment 3": [
            "Immunosuppressants",
            "Avoidance of irritants",
            "Oral antibiotics (severe cases)",
            "Wash bedding and clothing in hot water",
            "Systemic corticosteroids (severe cases)",
            "Hair transplant",
            "Systemic medications (e.g., methotrexate, cyclosporine)",
            "Shampoo containing selenium sulfide or zinc pyrithione",
            "Stress management",
            "Selenium sulfide shampoo"
        ]
    }

    df = pd.DataFrame(data)

    st.title("Hair Conditions and Treatments")
    st.table(df.style.set_properties(**{'text-align': 'left'}).set_table_styles([
    {'selector': 'th', 'props': [('color', 'black'), ('background-color', '#f2f2f2')]},
    {'selector': 'td', 'props': [('color', 'black')]}
    ]))
