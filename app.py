import streamlit as st
import requests

st.header("Ride Parameters")

# Date and time input
date = st.date_input('date')
time = st.time_input('time')

# Coordinates input
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

# Passenger count input
passenger_count = st.number_input('passenger count', min_value=1, max_value=8, value=1)

# Build the dictionary with the parameters for the API call
ride_params = {
    "pickup_datetime": f"{date} {time}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

url = 'https://taxifare.lewagon.ai/predict'

# Button to trigger the API call
if st.button('Get Fare Prediction'):
    response = requests.get(url, params=ride_params)
    
    # Handle the response from the API
    if response.status_code == 200:
        prediction = response.json().get('fare', 'No fare returned')
        st.success(f"The predicted fare is: ${prediction}")
    else:
        st.error("There was an error with the prediction request.")
