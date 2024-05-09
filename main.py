import streamlit as st
st.write("# **Anime**")
st.write("# Text to Image generator")
import requests

API_URL = "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.1"
headers = {"Authorization": "Bearer 9e10a3ea36b4872f2c60378e82e8600a"}

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
