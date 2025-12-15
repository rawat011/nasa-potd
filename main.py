import streamlit as st
import requests
import datetime
today_date = datetime.date.today()
potd_url = f"https://api.nasa.gov/planetary/apod?api_key=RNSXJd5RsHie92R4SaA9j7h3IChATW9AhoH7RcLA&date={today_date}"

# get potd content
response = requests.get(potd_url)
content = response.json()

# download the image
img_video_url = content["url"]

# If not an image, display previous day image
if img_video_url.endswith(".jpg"):
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








