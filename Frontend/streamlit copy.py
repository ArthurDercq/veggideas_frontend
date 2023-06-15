import streamlit as st
from PIL import Image
import requests
import pandas as pd
from filter_df import filter_dataframe
from streamlit_option_menu import option_menu



api_url = "https://veggideas-5s5h4zi4hq-ew.a.run.app"
api_url = api_url + "/predict"




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
        # Upload Page
        st.title("Vegetable Recognition")
        st.markdown("### Let's do vegetable recognition 👇")
        img_file_buffer = st.file_uploader('Upload an image')

        if img_file_buffer is not None:
            # Display the image uploaded by the user
            image = Image.open(img_file_buffer)
            st.image(image, caption="Here's the image you uploaded ☝️")

            # Make predictions when the user clicks the button
            if st.button("Make predictions"):
                with st.spinner("Wait for it..."):
                    # Send the image to the API endpoint
                    image_bytes = img_file_buffer.getvalue()
                    st.write("Sending image to the API...")

                    # Use 'rb' if you get an error about 'bytes-like object is required, not str'
                    response = requests.post(api_url, files={'img': image_bytes})

                    if response.status_code == 200:
                        # Parse the predictions from the JSON response
                        data = response.json()
                        st.write(data[0])
                        df = pd.DataFrame(data[2])
                        st.write(df)

                        # Filtering option
                        modify = st.checkbox("Filter result?")
                        if modify:
                            filtered_df = filter_dataframe(df)
                            st.write(filtered_df)
                        else:
                            st.write(df)

                    else:
                        st.error("Error making predictions. Please try again.")

if __name__ == "__main__":
    main()
