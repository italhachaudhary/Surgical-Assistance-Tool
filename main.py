import streamlit as st

st.set_page_config(page_title="Surgical Assistance Tool", layout="wide")
st.title("🧠 Surgical Assistance Tool")

tab1, tab2 = st.tabs(["📤 Upload Image", "📸 Live Detection"])

with tab1:
    exec(open("image_detector_app.py").read())

with tab2:
    exec(open("testWith_camera.py").read())
