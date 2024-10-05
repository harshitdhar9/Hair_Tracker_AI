import streamlit as st

def run_page():

    st.markdown("""
        <style>
        .stForm {
            padding: 10px;
            border-radius: 30px;
            border: 2px solid #2c3e50;
            background-color: #f7bfa8;
        }
        @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
        }
        h2 {
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
        <h2>
        <b>
            HairFall Prediction
        </b>
        </h2>
    """, unsafe_allow_html=True)

    col_x,col_y=st.columns(2)

    with col_x:
        st.markdown("<h3 style='text-align: center;'>𝙷𝚊𝚒𝚛 𝙻𝚘𝚜𝚜 𝙿𝚛𝚎𝚍𝚒𝚌𝚝𝚒𝚘𝚗</h3>",unsafe_allow_html=True)
    
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
            
            col3, col4, col5 = st.columns([1,2,1])
        
            with col4:
                submit_button = st.form_submit_button("​⨳ 𝗦𝘂𝗯𝗺𝗶𝘁 𝘁𝗼 𝗔𝗻𝗮𝗹𝘆𝘀𝗲 ⨳",use_container_width=True)

                if submit_button:
                    if not(genetics and hormonal_changes and medical_conditions and medications_treatments and nutritional_deficiencies and stress and age and poor_hair_care and environmental_factors and smoking and weight_loss):
                        st.error("Please fill in all required fields marked with *")
                    else:
                        st.success("Form submitted successfully!")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    col_z, col_a = st.columns([2,1])
    with col_y:
        st.markdown("<h3 style='text-align: center;'>𝙷𝚊𝚒𝚛 𝙵𝚊𝚕𝚕 𝙿𝚛𝚎𝚍𝚒𝚌𝚝𝚒𝚘𝚗</h3>",unsafe_allow_html=True)
    
        with st.form("Form 2",clear_on_submit=True):
            st.markdown('<div>', unsafe_allow_html=True)
            col10, col20 = st.columns(2)
            with col10:
                iron = st.text_input("𝙄𝙧𝙤𝙣 *")
                vitamin = st.text_input("𝙑𝙞𝙩𝙖𝙢𝙞𝙣 *")
                protein = st.text_input("𝙏𝙤𝙩𝙖𝙡 𝙋𝙧𝙤𝙩𝙚𝙞𝙣 *")
                manganese = st.text_input("𝙈𝙖𝙣𝙜𝙖𝙣𝙚𝙨𝙚 *")
        
            with col20:
                liver = st.text_input("𝙇𝙞𝙫𝙚𝙧 𝘿𝙖𝙩𝙖 *")
                calcium = st.text_input("𝘾𝙖𝙡𝙘𝙞𝙪𝙢 *")
                keratine = st.text_input("𝙏𝙤𝙩𝙖𝙡 𝙆𝙚𝙧𝙖𝙩𝙞𝙣𝙚 *")
                 
            col30, col40, col50 = st.columns([1,2,1])
        
            with col40:
                submit_button = st.form_submit_button("⨳ 𝗦𝘂𝗯𝗺𝗶𝘁 𝘁𝗼 𝗣𝗿𝗲𝗱𝗶𝗰𝘁 ⨳",use_container_width=True)

                if submit_button:
                    if not(iron and vitamin and protein and manganese and liver and calcium and keratine):
                        st.error("Please fill in all required fields marked with *")
                    else:
                        st.success("Form submitted successfully!")
            
            st.markdown('</div>', unsafe_allow_html=True)
    