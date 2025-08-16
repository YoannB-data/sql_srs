import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review ?",
    ("Joins", "GroupBy", "Window functions"),
    index = None,
    placeholder="Select a theme..."
)

st.write(f"You have selected {option}")

data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)

input_text = st.text_area("Enter SQL request : ")
if input_text is not None:
    st.dataframe(duckdb.sql(input_text))


