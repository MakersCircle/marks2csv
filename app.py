import streamlit as st
from PIL import Image
import numpy as np
from src.image_interpreter import ImageInterpreter
import pandas as pd
import streamlit.components.v1 as components

st.title('Marks2CSV')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
st.write("UPLOADED FILE : ")
if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    image_array = np.array(image_data)
    image_analyser = ImageInterpreter(image_array)
    image_analyser.extract()
    marks_dict = image_analyser.marks
    marks = {}
    confidence = {}
    for key, values in marks_dict.items():
        marks[key] = [val[0] for val in values]
        confidence[key] = [val[1] for val in values]
    def style_based_on_confidence(mark_df, confidence_df, threshold=0.90):
        # Create a function to apply style based on confidence
        def apply_style(v, c):
            if v == 0:
                return 'color: #427AA1'
            elif c > threshold:
                return 'color: #70F8BA'
            else:
                return 'color: #EB5160'

        # Create a new styled object
        styled = mark_df.style.apply(lambda x: [apply_style(v, c) for v, c in zip(x, confidence_df[x.name])], axis=0)
        return styled


    styled_result = style_based_on_confidence(pd.DataFrame(marks), pd.DataFrame(confidence))

    editable = not st.toggle("Edit")

    a = st.data_editor(styled_result, disabled=editable)
    df_data = []
    for key, values in marks_dict.items():
        for i, (mark, confidence) in enumerate(values, 1):
            df_data.append({
                'Question No': key,
                'Subpart': chr(96 + i),
                'Mark': mark,
                'Confidence': confidence
            })
    df = pd.DataFrame(df_data)
    st.image(image_data, caption='UPLOADED IMAGE:')
    st.write("PROCESSED MARKS:")
    total_marks = df['Mark'].apply(pd.to_numeric, errors='coerce').sum()
    st.write("TOTAL = ", total_marks)
    st.dataframe(df)
else:
    st.write("Please upload an image to proceed.")
