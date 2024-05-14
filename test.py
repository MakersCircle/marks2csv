import re
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

# from src.image_interpreter import ImageInterpreter


st.set_page_config(page_title="marks2CSV", layout="wide")

if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = None
if 'data' not in st.session_state:
    st.session_state.data = None
if 'title' not in st.session_state:
    st.session_state.title = None
if 'source' not in st.session_state:
    st.session_state.source = "Source"
if 'image' not in st.session_state:
    st.session_state.image = None

table = {}
for i in range(1, 13):
    table[i] = [0] * 3

if 'marks' not in st.session_state:
    st.session_state.marks = table
if 'confidence' not in st.session_state:
    st.session_state.confidence = table
if 'roll_no' not in st.session_state:
    st.session_state.roll_no = None
if 'roll_no_list' not in st.session_state:
    st.session_state.roll_no_list = None


def mark_column_splitting(column_name):
    parts = re.match(r'(\d+)(?:\.([a-z]))?\s*\((\d+\.\d+)\)\s*(\w+)', column_name)

    q_no = int(parts.group(1))
    subpart = None if parts.group(2) is None else ord(parts.group(2)) - ord('a')
    max_mark = float(parts.group(3))

    return q_no, subpart, max_mark


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


if st.session_state.uploaded_data is None:
    uploaded_file = st.file_uploader("Please upload your CSV file from Etlab", type=['csv'])
    if uploaded_file is not None:
        st.session_state.uploaded_data = pd.read_csv(uploaded_file)
        # st.session_state.title = add title of the uploaded_file
        # st.session_state.data = add data after removing the title
        # st.session_state.roll_no_list = st.session_state.data['Roll No'].to_list()
        # st.session_state.roll_no = st.session_state.roll_no_list[0]
        st.experimental_rerun()

if st.session_state.uploaded_data is not None:
    # Display the rest of the app after the file is uploaded
    with st.sidebar.popover("Source"):
        st.session_state.source = st.radio("Select source for input image",
                                           ["Upload Image", "Camera"],
                                           index=None)

    image_section, table_section = st.columns([1, 2])

    with image_section:

        # code to display name and roll number
        # st.write(st.session_state.data.loc[st.session_state.data[st.session_state.data['Roll No'] == st.session_state.roll_no].index.tolist()[0],"Name"])
        image_array = None
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

        if image_array is not None:
            # image_analyser = ImageInterpreter(image_array)
            # image_analyser.extract()
            # st.session_state.marks = image_analyser.marks
            # st.session_state.confidence = image_analyser.confidence
            # warped_image = image_analyser.warped_image

            st.session_state.marks = {1: ['2', '0', '0'],
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

            st.session_state.confidence = {1: [0.989, 0.995, 1.0],
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
            st.image(warped_image, caption="Uploaded Image", width=500)

        else:
            st.image("https://placehold.co/500x634?text=Provide+an+image", width=500)

    with table_section:
        styled_marks = style_based_on_confidence(pd.DataFrame(st.session_state.marks),
                                                 pd.DataFrame(st.session_state.confidence))
        editable = not st.toggle("Edit")
        a = st.data_editor(styled_marks, disabled=editable)
        if st.button("Next"):
            # add the detected marks 'a' to the st.session_state.data
            # update st.session_state.uploaded_data with updated st.session_state.data
            # change rollnumber to next
            # make st.session_state.marks  and st.session_state.confidence to null
            # st.session_state.image = None:
            pass
        st.dataframe(st.session_state.uploaded_data)
        updated_data = st.session_state.uploaded_data
        # download button
