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
    
    def generate_html_table(df):
        questions = df['Question No'].unique()
        subparts = sorted(df['Subpart'].unique())
        html = '<table style="border-collapse: collapse; width: 100%;background-color: white;">'
        html += '<tr><th></th>' + ''.join(f'<th style="border: 1px solid black; padding: 5px; text-align: center;">{q}</th>' for q in questions) + '</tr>'
        for subpart in subparts:
            html += f'<tr><td style="border: 1px solid black; padding: 5px;">{subpart.upper()}</td>'
            for question in questions:
                entry = df[(df['Question No'] == question) & (df['Subpart'] == subpart)]
                if not entry.empty:
                    mark = entry.iloc[0]['Mark']
                    conf = entry.iloc[0]['Confidence']
                    color = 'green' if conf > 0.8 else 'yellow' if conf > 0.5 else 'red'
                    html += f'<td style="border: 1px solid black; background-color: {color};"><input type="text" value="{mark}" style="width: 100%; background: transparent; border: none; text-align: center;" onclick="this.select();"></td>'
                else:
                    html += '<td style="border: 1px solid black;"></td>'
            html += '</tr>'
        html += '</table>'
        return html
    html_table = generate_html_table(df)
    st.image(image_data, caption='UPLOADED IMAGE:')
    st.write("PROCESSED MARKS:")
    components.html(html_table, height=130)
    total_marks = df['Mark'].apply(pd.to_numeric, errors='coerce').sum()
    st.write("TOTAL = ", total_marks)
else:
    st.write("Please upload an image to proceed.")
