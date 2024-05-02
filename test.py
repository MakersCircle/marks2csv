import streamlit as st
import pandas as pd
import numpy as np

# Sample DataFrame
mark = pd.DataFrame({
    "1": [3,0,0],
    "2": [2.5,0,0]})
confidence = pd.DataFrame({
    "1": [.95,1,1],
    "2": [.89,1,1]})


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


styled_result = style_based_on_confidence(mark, confidence)

editable = not st.toggle("Edit")

a = st.data_editor(styled_result, disabled=editable)
print(a)

