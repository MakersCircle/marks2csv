import cv2

# from src.image_interpreter import ImageInterpreter

import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st


st.set_page_config(page_title="marks2CSV", layout="wide")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
st.write("UPLOADED FILE : ")
if uploaded_file is not None:
    # image_data = Image.open(uploaded_file)
    # image_array = np.array(image_data)
    # image_analyser = ImageInterpreter(image_array)
    # image_analyser.extract()
    # marks = image_analyser.marks
    # confidence = image_analyser.confidence
    # warped_image = image_analyser.warped_image

    marks = {1: ['2', '0', '0'],
             2: ['0', '0', '0'],
             3: ['1.5', '0', '0'],
             4: ['6.5', '0', '0'],
             5: ['0', '0', '0'],
             6: ['7', '0', '0'],
             7: ['0', '0', '0'],
             8: ['7', '0', '0'],
             9: ['7', '0', '0'],
             10: ['1', '0', '0'],
             11: ['0', '0', '0'],
             12: ['7', '0', '0']}

    confidence = {1: [0.989, 0.995, 1.0],
                  2: [0.997, 1.0, 1.0],
                  3: [0.998, 1.0, 0.997],
                  4: [0.97, 1.0, 1.0],
                  5: [0.999, 0.999, 1.0],
                  6: [1.0, 0.999, 1.0],
                  7: [0.998, 0.999, 1.0],
                  8: [1.0, 1.0, 1.0],
                  9: [1.0, 1.0, 1.0],
                  10: [0.857, 1.0, 1.0],
                  11: [1.0, 1.0, 1.0],
                  12: [1.0, 1.0, 1.0]}

    warped_image = cv2.imread('test_images/warpped/scanned1.jpg')

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


    styled_marks = style_based_on_confidence(pd.DataFrame(marks), pd.DataFrame(confidence))
    st.image(warped_image, caption="Uploaded Image", width=500)

    editable = not st.toggle("Edit")
    a = st.data_editor(styled_marks, disabled=editable)
else:
    st.write("Please upload an image to proceed.")
