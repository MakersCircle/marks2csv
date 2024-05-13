import cv2

# from src.image_interpreter import ImageInterpreter

import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

st.set_page_config(page_title="marks2CSV", layout="wide")

if 'data' not in st.session_state:
    st.session_state.data = None
if 'source' not in st.session_state:
    st.session_state.source = "Source"
if 'image' not in st.session_state:
    st.session_state.image = None

table = {}
for i in range(1,13):
    table[i+1] = [0]*3

if 'marks' not in st.session_state:
    st.session_state.marks = table
if 'confidence' not in st.session_state:
    st.session_state.confidence = table
if 'roll_no' not in st.session_state:
    st.session_state.roll_no = None
if 'roll_no_list' not in st.session_state:
    st.session_state.roll_no_list = None


def style_based_on_confidence(mark_df, confidence_df, threshold=0.90):
    def apply_style(v, c):
        if v == '0':
            return 'color: #427AA1'
        elif c > threshold:
            return 'color: #70F8BA'
        else:
            return 'color: #EB5160'

    styled = mark_df.style.apply(lambda x: [apply_style(v, c) for v, c in zip(x, confidence_df[x.name])], axis=0)
    return styled


if st.session_state.data is None:
    uploaded_file = st.file_uploader("Please upload your CSV file from Etlab", type=['csv'])
    if uploaded_file is not None:
        st.session_state.data = pd.read_csv(uploaded_file)
        st.experimental_rerun()

if st.session_state.data is not None:
    # Display the rest of the app after the file is uploaded
    with st.sidebar.popover("Source"):
        st.session_state.source = st.radio("Select source for input image",
                                           ["Upload Image", "Camera"],
                                           index=None)

    image_section, table_section = st.columns([1, 2])

    with image_section:

        if st.session_state.source == "Upload Image":
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
            if uploaded_file is not None:
                image_data = Image.open(uploaded_file)
                image_array = np.array(image_data)
        elif st.session_state.source == "Camera":
            img_file_buffer = st.camera_input("Take a picture")
            if img_file_buffer is not None:
                img = Image.open(img_file_buffer)
                img_array_unrotated = np.array(img)
                image_array = np.rot90(img_array_unrotated, k=-1)
            st.info("Wont work. Under construction")
        else:
            st.error("Select an image source")


        warped_image = cv2.imread('test_images/warpped/scanned1.jpg')




        if st.session_state.image is None:
            st.image("https://placehold.co/500x634?text=Provide+an+image", width=500)
        else:
            st.image(warped_image, caption="Uploaded Image", width=500)

    with table_section:
        st.dataframe(st.session_state.data)
