import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

'''
# TaxiFareModel front
'''


st.markdown('''
Welcome to the veggideas website
''')
def main():
    st.markdown('''
        #Welcome to the veggideas website
        ''')
    # Set the title of the app
    st.markdown("##Recipe generator")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Make predictions when the user clicks the button
        if st.button('Make Predictions'):
            # Call the function to make predictions using your API
            predictions = "carrot"

            # Display the predictions
            st.subheader("Predictions:")
            for i, prediction in enumerate(predictions):
                st.write(f"{i+1}. {prediction}")
