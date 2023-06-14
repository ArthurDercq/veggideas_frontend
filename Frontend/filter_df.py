import pandas as pd
from pandas.api.types import is_categorical_dtype, is_numeric_dtype
import streamlit as st

#def filter_dataframe(df: dict, to_filter_columns) -> dict:
def filter_dataframe(df):
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (dict): Original dataframe as a dictionary of recipe details

    Returns:
        dict: Filtered dataframe as a dictionary
    """

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if isinstance(df[column], list) and len(set(df[column])) < 100:
                user_cat_input = st.selectbox(
                    f"Values for {column}",
                    list(set(df[column])),
                    default=list(set(df[column])),
                )
                df = {k: v for k, v in df.items() if k == column or v in user_cat_input}

            elif all(isinstance(val, (int, float)) for val in df[column]):
                _min = float(min(df[column]))
                _max = float(max(df[column]))
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df.Time <= user_num_input[1]]
            elif len(set(df[column])) > 100:
                meal_type = st.selectbox(
                f"Values for {column}",
                [item for sublist in meal_type for item in sublist],
                default=None,
                )
                df = {k: v for k, v in df.items() if k == column or any(meal_type_word in v for meal_type_word in meal_type)}

            else:
                user_text_input = right.selectbox(
                f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = {k: v for k, v in df.items() if k == column or (isinstance(v, str) and user_text_input in v)}

        return df
