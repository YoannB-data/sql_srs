# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage, price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution_df = duckdb.sql(ANSWER_STR).df()


st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice
"""
)


with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?", ("Joins", "GroupBy", "Window functions"),index=None,
        placeholder="Select a theme...",
    )
    st.write(f"You have selected {option}")


st.header("Enter your code :")
query = st.text_area(label="Enter SQL request : ", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    # Column checks
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    # Line checks
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write("Some lines are missing")


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_STR)
