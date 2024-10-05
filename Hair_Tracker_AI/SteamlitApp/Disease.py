import streamlit as st

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

def run_page():
    st.markdown('<div class="image-uploader"><h3>Upload the image of area affected by hair disease</h3></div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label="Choose a jpeg, jpg file", type=('jpg', 'jpeg'), key='file-upload1', help='Upload a .jpg or .jpeg image')
        
    if uploaded_file is not None:
        st.markdown('<div class="uploaded-image">', unsafe_allow_html=True)
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown('<div class="image-uploader"><h3>Upload the image of your hair to get hair type</h3></div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label="Choose a jpeg, jpg file", type=('jpg', 'jpeg'), key='file-upload2', help='Upload a .jpg or .jpeg image')
        
    if uploaded_file is not None:
        st.markdown('<div class="uploaded-image">', unsafe_allow_html=True)
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)