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
        filtered_columns = ["Time", "Meal Type", "Diet Type", "Cuisine", "Ingredients"]
        to_filter_columns = st.multiselect("Filter recipes on", filtered_columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")

            if all(isinstance(val, (int, float)) for val in df[column]):
                _min = float(min(df[column]))
                _max = float(max(df[column]))
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Cooking time {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df.Time <= user_num_input[1]]

            elif column == "Meal Type":
                meal_type = right.selectbox("Choose your mealtype", get_values(df[column]))
                df = df[df["Meal Type"].apply(lambda x: meal_type in x)]

            elif column == "Diet Type":
                options = right.multiselect("Choose a diet from the options", get_values(df[column]))
                df = df[df["Diet Type"].apply(lambda x: all(option in x for option in options))]

            elif column == "Cuisine":
                cuisine = right.multiselect("Choose a cuisine from the options", df[column].unique())
                if cuisine:
                    df = df[df["Cuisine"].apply(lambda x: x in cuisine)]

            elif column == "Ingredients":
                user_text_input = right.text_input(
                    f"Which ingredient do you want to add",
                    )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input, case=False)]


        return df


def get_values(column):
    values = set()
    for list in column:
        for word in list:
            values.add(word)
    return values
