from src.image_interpreter import ImageInterpreter

import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st


st.title('Marks2CSV')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
st.write("UPLOADED FILE : ")
if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    image_array = np.array(image_data)
    image_analyser = ImageInterpreter(image_array)
    image_analyser.extract()
    marks = image_analyser.marks
    confidence = image_analyser.confidence


    def style_based_on_confidence(mark_df, confidence_df, threshold=0.90):
        def apply_style(v, c):
            if v == 0:
                return 'color: #427AA1'
            elif c > threshold:
                return 'color: #70F8BA'
            else:
                return 'color: #EB5160'

        styled = mark_df.style.apply(lambda x: [apply_style(v, c) for v, c in zip(x, confidence_df[x.name])], axis=0)
        return styled


    styled_marks = style_based_on_confidence(pd.DataFrame(marks), pd.DataFrame(confidence))

    editable = not st.toggle("Edit")
    a = st.data_editor(styled_marks, disabled=editable)
else:
    st.write("Please upload an image to proceed.")
