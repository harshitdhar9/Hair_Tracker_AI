import streamlit as st

st.set_page_config(
    page_title="Hair Tracker AI",
    layout="wide",
)

from Hairfall import run_page as run_page1
from Disease import run_page as run_page2
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title="Navigation",
        options=["Home","HairFall Prediction","Disease Classification"],
        icons=["🏠","💇‍♂️","☠️"],
        menu_icon="cast",
        default_index=0
    )

if selected=="Home":
    st.title("Welcome to Hair Tracker AI")
if selected=="HairFall Prediction":
    run_page1()
if selected=="Disease Classification":
    run_page2()