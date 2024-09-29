#Importing libraries 
import numpy as np
import streamlit as st
from PIL import Image
# from pyngrok import ngrok
# import finalModel # call Model from the python file

# Set the page configuration to use the full width
# st.set_page_config(layout="wide")

# Set the background image
# background_image = "ImgCptnBckgrnd.jpeg"
# background_image = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366"

# st.markdown(f"""
# <style>
#     .reportview-container {{
#         background-image: url('{background_image}');
#         background-size: cover;
#         background-position: center;
#     }}
# </style>
# """, unsafe_allow_html=True)


# Load custom CSS
st.markdown("""
    <style>
    .title {
        font-family: 'Century Gothic (Headings)'monospace;
        font-size: 48px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-family: 'Century Gothic (Body)', sans-serif;
        font-size: 24px;
        color: #4CAF50;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">Automatic Image Captioning</div>', unsafe_allow_html=True)

# Define functions for each option
def RES_LSTM_8k():
    import modelRES_LSTM_8k

    # st.write("Encoder RES - Decoder LSTM - 8k Dataset: ")
    if uploaded_file is not None:
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("RES - LSTM - 8k")

        caption = modelRES_LSTM_8k.predict_step(uploaded_file)
        # st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)
        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)

def RES_LSTM_30k():
    import modelRES_LSTM_30k

    # st.write("Encoder RES - Decoder LSTM - 30k Dataset: ")
    if uploaded_file is not None:
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("RES - LSTM - 30k")

        caption = modelRES_LSTM_30k.predict_step(uploaded_file)
        # st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)
        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)

def CLIP_LSTM_8k():
    import modelCLIP_LSTM_8k

    # st.write("Encoder CLIP - Decoder LSTM - 8k Dataset: ")
    if uploaded_file is not None:
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("CLIP - LSTM - 8k")

        caption = modelCLIP_LSTM_8k.predict_step(uploaded_file)
        # st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)
        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)

def CLIP_LSTM_30k():
    import modelCLIP_LSTM_30k

    # st.write("Encoder CLIP - Decoder LSTM - 30k Dataset: ")
    if uploaded_file is not None:
        # st.write("image type : ", type(image), " : ", image)
        
        # st.write("uploaded_file type : ", type(uploaded_file), " : ", uploaded_file)
        # caption = modelCLIP_LSTM_30k.predict_step(image)
        
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("CLIP - LSTM - 30k")

        caption = modelCLIP_LSTM_30k.predict_step(uploaded_file)

        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)

def CLIP_ATTN_8k():
    import modelCLIP_ATTN_8k
    # st.write("Encoder CLIP - Decoder ATTN - 8k Dataset: ")
    if uploaded_file is not None:
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("CLIP - Attn+LSTM - 8k")

        caption = modelCLIP_ATTN_8k.predict_step(uploaded_file)
        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)

def CLIP_ATTN_30k():
    import modelCLIP_ATTN_30k
    # st.write("Encoder CLIP - Decoder ATTN - 30k Dataset: ")
    if uploaded_file is not None:
        #   st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("CLIP - Attn+LSTM - 30k")

        caption = modelCLIP_ATTN_30k.predict_step(uploaded_file)
        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption}</div>', unsafe_allow_html=True)

def VITmodel():
    import modelVIT
    # st.write("Encoder VIT - Decoder GPT2: ")
    if uploaded_file is not None:
        # Create two columns
        col1, col2 = st.columns([1,4])
        # Add content to the first column
        with col1:
            st.write("VIT - GPT2 - Pretrain")

        caption = modelVIT.predict_step(image)
        # Add content to the second column
        with col2:
            st.markdown(f'<div class="subtitle">{caption[0]}</div>', unsafe_allow_html=True)

# Create a grid with two columns
col1, col2 = st.columns(2)

picture = None
uploaded_file = None
# Add buttons to each column
with col1:
    # if st.button("Camera"):
    st.write("Taking Picture from Camera")
    picture = st.camera_input("")

with col2:
    # Option to upload an image file
    st.write("Or Upload an Image")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

# Display the captured or uploaded image
if picture:
    # st.write("Picture NOT None: " + picture)
    uploaded_file = None
    uploaded_file = picture

# Display the uploaded image
if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("Image uploaded successfully.")
    image = image.resize((224, 224))
    # st.image(image, caption="Uploaded 224x224 Image.", use_column_width=True)
    
# VIT - GPT2 - Pretrain
# CLIP - Attn+LSTM - 30k 
# CLIP - Attn+LSTM - 8k
# CLIP - LSTM - 30k
# CLIP - LSTM - 8k
# RES - LSTM - 30k
# RES - LSTM - 8k

# Create a select box for Image Caption Predection Model
option = st.selectbox(
    "Choose an Image Caption Predection Model:",
    (""
     , "All"
     , "VIT - GPT2 - Pretrain"
     , "CLIP - Attn+LSTM - 30k"
     , "CLIP - Attn+LSTM - 8k"
     , "CLIP - LSTM - 30k"
     , "CLIP - LSTM - 8k"
     , "RES - LSTM - 30k"
     , "RES - LSTM - 8k"
    )
)

# Execute corresponding function based on selected option
if option == "RES - LSTM - 8k":
    RES_LSTM_8k()
elif option == "RES - LSTM - 30k":
    RES_LSTM_30k()
elif option == "VIT - GPT2 - Pretrain":
    VITmodel()
elif option == "CLIP - LSTM - 8k":
    CLIP_LSTM_8k()
elif option == "CLIP - LSTM - 30k":
    CLIP_LSTM_30k()
elif option == "CLIP - Attn+LSTM - 8k":
    CLIP_ATTN_8k()
elif option == "CLIP - Attn+LSTM - 30k":
    CLIP_ATTN_30k()
elif option == "All":
    VITmodel()
    CLIP_ATTN_8k()
    CLIP_ATTN_30k()
    CLIP_LSTM_8k()
    CLIP_LSTM_30k()
    RES_LSTM_8k()
    RES_LSTM_30k()

