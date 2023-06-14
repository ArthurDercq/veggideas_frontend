import streamlit as st
from PIL import Image
import requests
import io
import pandas as pd
from filter_df import filter_dataframe

# Set page tab display
st.set_page_config(
    page_title="Simple Image Uploader",
    page_icon='🖼️',
    layout="wide",
    initial_sidebar_state="expanded",
)

# API URL for vegetable recognition
api_url = "https://veggideas-5s5h4zi4hq-ew.a.run.app"

# App title and description
st.header('Simple Image Uploader 📸')
st.markdown('''
            > This is a Le Wagon boilerplate for any data science projects that involve exchanging images between a Python API and a simple web frontend.

            > **What's here:**

            > * [Streamlit](https://docs.streamlit.io/) on the frontend
            > * [FastAPI](https://fastapi.tiangolo.com/) on the backend
            > * [PIL/pillow](https://pillow.readthedocs.io/en/stable/) and [opencv-python](https://github.com/opencv/opencv-python) for working with images
            > * Backend and frontend can be deployed with Docker
            ''')

st.markdown("---")

### Create a native Streamlit file upload input
st.markdown("### Let's do vegetable recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:
    # Display the image uploaded by the user
    image = Image.open(img_file_buffer)
    st.image(image, caption="Here's the image you uploaded ☝️")
    #st.write("Any other preferences?")
    #vegetarian = st.checkbox('vegetarian')
    #vegan = st.checkbox('vegan')
    #pescatarian = st.checkbox('pescatarian')
    #surprise = st.checkbox('surprise me')
    # Make predictions when the user clicks the button
    with st.form("Basic form"):
        modify = st.checkbox("Add filters")
        #make_predictions = st.button("Make predictions")
        submitted = st.form_submit_button("Make predictions")
        if submitted:
         st.write("predictions")

        with st.spinner("Wait for it..."):
            # Send the image to the API endpoint
            image_bytes = img_file_buffer.getvalue()

            st.write("Sending image to the API...")

            # Use 'rb' if you get an error about 'bytes-like object is required, not str'
            api_url = api_url + "/predict"
            response = requests.post(api_url, files={'img': image_bytes})
            #response = st.cache_data(response)
            st.write(response.status_code)
            st.write(response.raise_for_status)
            if response.status_code == 200:
                # Parse the predictions from the JSON response
                data = response.json()
                # Create a DataFrame from the predictions data
                df = pd.DataFrame(data)

                # Create a DataFrame from the predictions data
                # Create a DataFrame from the predictions data
                if modify:
                    to_filter_columns = st.multiselect("Filter dataframe on", list(df.keys()))
                    df = filter_dataframe(df, to_filter_columns)
                st.dataframe(df)
                """
                if vegetarian:
                    st.dataframe(df[df['Diet Type'].apply(lambda x: 'Vegetarian' in x)])
                if vegan:
                    st.dataframe(df[df['Diet Type'].apply(lambda x: 'Vegan' in x)])
                if pescatarian:
                    st.dataframe(df[df['Diet Type'].apply(lambda x: 'Pescatarian' in x)])
                if vegetarian and vegan:
                    st.dataframe(df[df['Diet Type'].apply(lambda x: 'Vegan' and 'Vegetarian' in x)])
                if surprise:
                    st.dataframe(df)"""

           # else:
                #st.error("Error making predictions. Please try again.")
