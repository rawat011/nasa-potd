import streamlit as st
import requests
date = "2025-11-23"
potd_url = f"https://api.nasa.gov/planetary/apod?api_key=RNSXJd5RsHie92R4SaA9j7h3IChATW9AhoH7RcLA&date={date}"

# get potd content
response = requests.get(potd_url)
content = response.json()

# download the image
img_video_url = content["url"]
response = requests.get(img_video_url)

# save the imgae
potd = "potd.jpg"
with open(potd, "wb") as file:
    file.write(response.content)

# crate web-page with all the info
title = content["title"]
explanation = content["explanation"]
st.title(title, text_alignment="center")
st.set_page_config(layout="wide")
st.image("potd.jpg")
st.write(explanation)








