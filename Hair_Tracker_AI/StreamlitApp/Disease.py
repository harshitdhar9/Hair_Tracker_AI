import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model(r'AI_Models\hair_disease_cnn_model (1).h5')

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

def run_page():
    st.markdown('<div class="image-uploader"><h3>Upload the image of area affected by hair disease</h3></div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label="Choose a jpeg, jpg file", type=('jpg', 'jpeg'), key='file-upload1', help='Upload a .jpg or .jpeg image')
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        class_idx = np.argmax(prediction, axis=1)[0]  
        st.write(f"Prediction: {prediction}")
            
    st.markdown('<div class="image-uploader"><h3>Upload the image of your hair to get hair type</h3></div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label="Choose a jpeg, jpg file", type=('jpg', 'jpeg'), key='file-upload2', help='Upload a .jpg or .jpeg image')
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