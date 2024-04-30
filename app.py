import streamlit as st
from PIL import Image
import numpy as np
from src.image_interpreter import ImageInterpreter
import pandas as pd

def main():
    st.title('Marks2CSV')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image_data = Image.open(uploaded_file)
        image_array = np.array(image_data)
        image_analyser = ImageInterpreter(image_array)
        image_analyser.extract()
        marks_dict = image_analyser.marks
        df_data = []

        for key, values in marks_dict.items():
            row = {'Student': key}
            for i, (mark, confidence) in enumerate(values, 1):
                row[chr(96 + i)] = mark
                row['Conf ' + chr(96 + i)] = confidence
            df_data.append(row)

        df = pd.DataFrame(df_data).set_index('Student')

        def color_marks(s):
            conf_key = 'Conf ' + s.name  # Corresponding confidence column name
            return ['background-color: {}'.format(
                'green' if conf > 0.8 else 'yellow' if conf > 0.5 else 'red')
                for conf in df.loc[s.index, conf_key]]

        mark_columns = [chr(96 + i) for i in range(1, 4)]
        styled_transposed_df = df[mark_columns].transpose().style.apply(color_marks, axis=1)
        st.image(image_data, caption='UPLOADED IMAGE:')
        st.write("PROCESSED MARKS:")
        st.dataframe(styled_transposed_df)
        total_marks = df[mark_columns].sum().sum()
        st.write("TOTAL = ", total_marks)
    else:
        st.write("Please upload an image to proceed.")