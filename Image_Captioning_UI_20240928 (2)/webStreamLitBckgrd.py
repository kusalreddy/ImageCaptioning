import base64
import streamlit as st

background_image = ".\ImgCptnBckgrnd.jpeg"
# background_image = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366"

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background: url(data:image/{"jpeg"};base64,{base64.b64encode(open(background_image, "rb").read()).decode()});
    }}
    </style>
    """,
    unsafe_allow_html=True,
    )