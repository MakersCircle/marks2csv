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
        warped_image = cv2.imread('test_images/warpped/scanned1.jpg')
        st.image(warped_image, caption="Uploaded Image", width=500)

    with table_section:
        st.dataframe(st.session_state.data)
