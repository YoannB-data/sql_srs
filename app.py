import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World!")
data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)

input_text = st.text_area("Enter SQL request : ")
if input_text is not None:
    st.dataframe(duckdb.sql(input_text))


