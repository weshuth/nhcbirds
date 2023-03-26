#pip install streamlit requests

import requests
import streamlit as st
from PIL import Image
from io import BytesIO
import datetime

EBIRD_API_KEY = eBird_api_key
API_BASE_URL = "https://api.ebird.org/v2"
# IMAGE_API_URL = "<YOUR_IMAGE_API_URL>"

st.title("Recent Bird Sightings in New Hanover County")


def get_recent_sightings():
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=30)
    url = f"{API_BASE_URL}/data/obs/US-NC-129/recent"
    params = {
        "back": 30,
        "key": EBIRD_API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


def get_bird_image(bird_name):
    params = {"bird_name": bird_name}
    response = requests.get(IMAGE_API_URL, params=params)
    img = Image.open(BytesIO(response.content))
    return img


sightings = get_recent_sightings()

for sighting in sightings:
    bird_name = sighting["comName"]
    bird_img = get_bird_image(bird_name)

    # Display bird info
    col1, col2 = st.columns(2)
    with col1:
        st.image(bird_img, width=200)
    with col2:
        st.header(bird_name)
        st.subheader(f'Rarity Score: {sighting["howMany"]}')
        st.write(f'Species Code: {sighting["speciesCode"]}')
        st.write(f'Observation Date: {sighting["obsDt"]}')
        # Add a small blurb about the bird
        st.write("Bird description or blurb goes here.")
        # Trending status could be calculated based on historical data or other factors
        st.write("Trending: Upward/Downward")
