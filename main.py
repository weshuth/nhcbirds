import requests
import streamlit as st
from PIL import Image
from io import BytesIO
import datetime

API_BASE_URL = "https://api.ebird.org/v2"

st.title("Recent Bird Sightings in New Hanover County")

def get_recent_sightings():
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=30)
    url = f"{API_BASE_URL}/data/obs/US-NC-129/recent"
    params = {
        "back": 30,
        "key": st.secrets["EBIRD_API_KEY"],
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

sightings = get_recent_sightings()

# Pagination
items_per_page = 10
page_number = st.number_input(
    label="Page Number", min_value=1, value=1, step=1, format="%i"
)
start_index = (page_number - 1) * items_per_page
end_index = start_index + items_per_page
sightings_to_display = sightings[start_index:end_index]

for sighting in sightings_to_display:
    bird_name = sighting.get("comName", "Unknown")
    rarity_score = sighting.get("howMany", "Unknown")
    species_code = sighting.get("speciesCode", "Unknown")
    observation_date = sighting.get("obsDt", "Unknown")

    # Display bird info
    col1, col2 = st.columns(2)
    with col1:
        # st.image(bird_img, width=200)  # Uncomment when you have an image API
        pass
    with col2:
        st.header(bird_name)
        st.subheader(f'Rarity Score: {rarity_score}')
        st.write(f'Species Code: {species_code}')
        st.write(f'Observation Date: {observation_date}')
        # Add a small blurb about the bird
        st.write("Bird description or blurb goes here.")
        # Trending status could be calculated based on historical data or other factors
        st.write("Trending: Upward/Downward")
