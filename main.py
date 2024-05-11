import streamlit as st
import io
import os
st.write("# **Anime**")
st.write("# Text to Image generator")
import requests

API_URL = "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.1"
headers = {"Authorization": "Bearer "+ st.secrets["API_KEY"]}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
x = st.text_input("**Enter the prompt**")
check = st.button("Submit")
if(check==True):
    st.write("### **Generating Image**")
    image_bytes = query({
    "inputs": x,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    image = (io.BytesIO(image_bytes))
    st.image(image)
    st.download_button(label="Download Image", data = image,file_name="AnimeImage.jpg")
