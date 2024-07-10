import streamlit as st
import requests
import json

# Define constants
API_KEY = "b3c62ae7f7ad5fc3cb0a7b56cb7cbda6"
API_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&units=metric"
ICONS_PATH = "images/"

# Function to fetch weather data
def get_weather(city):
    url = f"{API_URL}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to display weather information
def display_weather(data):
    weather_description = data['weather'][0]['main']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    st.write(f"Weather: {weather_description}")
    st.write(f"Temperature: {temperature} °C")
    st.write(f"Humidity: {humidity} %")
    st.write(f"Wind Speed: {wind_speed} km/hr")

    # Display weather icon based on weather description
    if weather_description == 'Clear':
        st.image(ICONS_PATH + 'clear.png', width=100)
    elif weather_description == 'Clouds':
        st.image(ICONS_PATH + 'clouds.png', width=100)
    elif weather_description == 'Drizzle':
        st.image(ICONS_PATH + 'drizzle.png', width=100)
    elif weather_description == 'Rain':
        st.image(ICONS_PATH + 'rain.png', width=100)
    elif weather_description == 'Mist':
        st.image(ICONS_PATH + 'mist.png', width=100)

# Streamlit app layout
def main():
    st.title('WeatherNow')
    st.subheader('Get the latest weather updates for any city')

    # Input for city name
    city = st.text_input('Enter city name')

    if st.button('Get Weather'):
        if city:
            try:
                # Fetch weather data
                data = get_weather(city)
                if data['cod'] == 200:
                    # Display weather information
                    display_weather(data)
                else:
                    st.error(f"Error: {data['message']}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()