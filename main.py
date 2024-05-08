from dotenv import find_dotenv,load_dotenv
import streamlit as st
# from transformers import pipeline
# Use a pipeline as a high-level helper
load_dotenv(find_dotenv())
from transformers import pipeline
def imagetotext(url):
    pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = pipe(url)
    return text
# def texttoimage(txxt):
#     pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")

# print(imagetotext("photo.jpg"))

st.write("# Text to Image generator")
import requests

API_URL = "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.1"
headers = {"Authorization": "Bearer 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"}

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
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image)
# load_dotenv(find_dotenv())
