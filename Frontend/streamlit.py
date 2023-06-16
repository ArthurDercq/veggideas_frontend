import streamlit as st
from PIL import Image
import requests
import io
import numpy as np
import pandas as pd
from filter_df import filter_dataframe
from streamlit_option_menu import option_menu


# Set page tab display

# API URL for vegetable recognition
api_url = "https://veggideas-5s5h4zi4hq-ew.a.run.app"
api_url = api_url + "/predict"





#st.markdown("<div style='text-align:center;padding:20px;background-color:#66BB6A;border-radius:10px;box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 6px 8px rgba(0, 0, 0, 0.1);'>"
            #"<h1 style='color:white;font-size:56px;font-weight:bold;font-family:\"EB Garamond\", Garamond, serif;'>Veggideas</h1>"
            #"</div>", unsafe_allow_html=True)

st.set_page_config(layout="wide")

image = Image.open("./Frontend/veggideas.png")

st.image(image)


st.markdown("---")
def main():
    def on_change(key):
        selection = st.session_state[key]


    selected_option = option_menu(None, ["Upload", "About us"],
                        icons=['cloud-upload', 'gear'],
                        on_change=on_change, key='menu_5', orientation="horizontal")
    if selected_option == "About us":
        # Home Page

        # Define page layout
        col1, col2 = st.columns([1, 2])

        # About Us text
        with col1:
            st.title("About Us")
            st.markdown("""
            Welcome to our culinary world! We are Arthur, Liesel, and Lennert – the passionate minds behind our company. Through our shared love for cooking and technology, we have embarked on a mission to revolutionize the way people find recipes and reduce food waste.

            """)


        # Vision section
        with col2:
            st.title("Our Vision")
            st.markdown("""
            #### Embrace Your Inner Chef
            We envision a world where cooking becomes a source of joy, creativity, and self-expression. Our platform is designed to empower individuals to embrace their inner chef, experiment with flavors, and discover new culinary horizons. Unleash your creativity in the kitchen and let your taste buds guide you on a culinary adventure!

            #### Foster Sustainability
            At our core, we are committed to promoting sustainability in the kitchen. By utilizing vegetable detection technology, we aim to reduce food waste by helping you make the most of your ingredients. Let's join hands in creating a greener future, one delicious meal at a time!

            #### Cultivate a Culinary Community
            We believe that food has the power to bring people together. Through our platform, we strive to build a vibrant community of passionate food lovers, where knowledge is shared, inspiration is ignited, and connections are formed. Let's cook, learn, and grow together!

            #### Pioneer Innovation
            We are relentless in our pursuit of innovation. As technology advances, so does our commitment to staying at the forefront of culinary advancements. By harnessing the potential of artificial intelligence and machine learning, we continuously improve our recipe recommendation algorithms to provide you with unparalleled culinary experiences.

            """)

    elif selected_option == "Upload":
        ### Create a native Streamlit file upload input



        st.markdown("""### Capture and upload a vegetable picture to discover amazing recipes👇""")
        img_file_buffer = st.file_uploader('### Upload your veggie')

        if img_file_buffer is not None:
            # Display the image uploaded by the user
            image = Image.open(img_file_buffer)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(' ')

            with col2:
                st.image(image, caption="Here's the image you uploaded ☝️", width=450)

            with col3:
                st.write(' ')




            # Make predictions when the user clicks the button
            #with st.form("Basic form"):
                #modify = st.checkbox("Add filters")
                #make_predictions = st.button("Make predictions")
                #submitted = st.form_submit_button("Make predictions")
                #if submitted:
                    #st.write("predictions")

            with st.spinner("Wait for it... Analyzing the image"):
                        # Send the image to the API endpoint
                    image_bytes = img_file_buffer.getvalue()

                        # Use 'rb' if you get an error about 'bytes-like object is required, not str'

                    response = requests.post(api_url, files={'img': image_bytes})
                        #response = st.cache_data(response)
                    if response.status_code == 200:
                        # Parse the predictions from the JSON response
                        st.markdown("##")

                        data = response.json()
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.write(' ')

                        with col2:
                            st.markdown(f"### I'm {np.round(data[1])}% sure that it's a {data[0]}!")

                        with col3:
                            st.write(' ')

                        st.markdown("##")
                        st.divider()
                        st.markdown(f"## Let's have a look at the recipes with {data[0]} 👇")
                        st.markdown("##")

                        df = pd.DataFrame(data[2])


                        filtering = st.container()
                        #df = filter_dataframe(df)
                        #st.dataframe(df)

                        with filtering:
                            modify = st.checkbox("Do you want to add filters?")
                            st.markdown("##")
                            if modify:
                                df = filter_dataframe(df)
                                st.dataframe(df)
                            else:
                                st.dataframe(df)

                    else:
                        st.error("Error making predictions. Please try again.")



if __name__ == "__main__":

    main()
