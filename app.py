import pandas as pd
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
    marks_dict=image_analyser.marks
    total_marks = sum(value[0] for value in marks_dict.values())
    st.image(image_data, caption='Uploaded Image')
    st.write("Processed Results:")
    df = pd.DataFrame.from_dict(marks_dict, orient='index', columns=['a', 'b', 'c'])
    st.write(df.T)
    st.write("TOTAL = ",total_marks)
