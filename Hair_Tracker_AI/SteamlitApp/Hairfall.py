import streamlit as st

def run_page():

    st.markdown("""
        <style>
        .stForm {
            padding: 10px;
            border-radius: 30px;
            border: 2px solid #2c3e50;
            background-color: #b2adf7;
        }
        @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
        }
        h1 {
            animation: fadeIn 4s ease-in-out;
            text-align: center;
            color: #010103;
            font-size: 50px;
            font-weight: bold;
        }
        
        .stTextInput{
            margin-bottom: 20px;
            border-radius: 10px;
        }
        .stTextInput input:focus {
            border-color: #0b0d0c;
            outline: none;
        }
        .stTextInput label {
            color: #12100f;
        }
        .stTextInput input {
            color: #0e0336;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h1>
        <b>
            HairFall Prediction
        </b>
        </h1>
    """, unsafe_allow_html=True)

    col_x,col_y=st.columns([2,1])

    with col_x:
        st.markdown("<h2 style='text-align: center;'>𝙷𝚊𝚒𝚛 𝙻𝚘𝚜𝚜 𝙿𝚛𝚎𝚍𝚒𝚌𝚝𝚒𝚘𝚗</h2>",unsafe_allow_html=True)
    
        with st.form("Form 1",clear_on_submit=True):
            st.markdown('<div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                genetics = st.text_input("𝙂𝙚𝙣𝙚𝙩𝙞𝙘𝙨 *")
                hormonal_changes = st.text_input("𝙃𝙤𝙧𝙢𝙤𝙣𝙖𝙡 𝘾𝙝𝙖𝙣𝙜𝙚𝙨 *")
                medical_conditions = st.text_input("𝙈𝙚𝙙𝙞𝙘𝙖𝙡 𝘾𝙤𝙣𝙙𝙞𝙩𝙞𝙤𝙣𝙨 *")
                medications_treatments = st.text_input("𝙈𝙚𝙙𝙞𝙘𝙖𝙩𝙞𝙤𝙣𝙨 & 𝙏𝙧𝙚𝙖𝙩𝙢𝙚𝙣𝙩𝙨 *")
                nutritional_deficiencies = st.text_input("𝙉𝙪𝙩𝙧𝙞𝙩𝙞𝙤𝙣𝙖𝙡 𝘿𝙚𝙛𝙞𝙘𝙞𝙚𝙣𝙘𝙞𝙚𝙨 *")
                stress = st.text_input("𝙎𝙩𝙧𝙚𝙨𝙨 *")
        
            with col2:
                age = st.text_input("𝘼𝙜𝙚 *")
                poor_hair_care = st.text_input("𝙋𝙤𝙤𝙧 𝙃𝙖𝙞𝙧 𝘾𝙖𝙧𝙚 𝙃𝙖𝙗𝙞𝙩𝙨 *")
                environmental_factors = st.text_input("𝙀𝙣𝙫𝙞𝙧𝙤𝙣𝙢𝙚𝙣𝙩𝙖𝙡 𝙁𝙖𝙘𝙩𝙤𝙧𝙨 *")
                smoking = st.text_input("𝙎𝙢𝙤𝙠𝙞𝙣𝙜 *")
                weight_loss = st.text_input("𝙒𝙚𝙞𝙜𝙝𝙩 𝙇𝙤𝙨𝙨 *")
            
            col3, col4, col5 = st.columns(3)
        
            with col4:
                submit_button = st.form_submit_button("𝐒𝐮𝐛𝐦𝐢𝐭",use_container_width=True)

                if submit_button:
                    if not(genetics and hormonal_changes and medical_conditions and medications_treatments and nutritional_deficiencies and stress and age and poor_hair_care and environmental_factors and smoking and weight_loss):
                        st.error("Please fill in all required fields marked with *")
                    else:
                        st.success("Form submitted successfully!")
            
            st.markdown('</div>', unsafe_allow_html=True)