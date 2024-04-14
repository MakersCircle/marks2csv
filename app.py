import streamlit as st
from PIL import Image
import numpy as np
from src.image_interpreter import ImageInterpreter
st.title('Marks2CSV')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    image_array = np.array(image_data)
    image_analyser = ImageInterpreter(image_array)
    image_analyser.extract()
    st.image(image_data, caption='Uploaded Image')
    st.write("Processed Results:")
    st.write(image_analyser)
