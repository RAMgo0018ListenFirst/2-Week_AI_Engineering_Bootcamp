# ============================================
# WEATHER APP USING REQUESTS + Pydantic
# WITH TIMEOUTS AND ASYNC FUNCTIONS
# ============================================

# -----------------------------
# IMPORTS
# -----------------------------

import os
import json
import asyncio
import requests

from dotenv import load_dotenv
from pydantic import BaseModel

# -----------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------

# Loads variables from .env file
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("API_KEY")

# -----------------------------
# PYDANTIC MODEL
# -----------------------------

# Pydantic validates and structures the data
class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: int
    condition: str

# -----------------------------
# ASYNC FUNCTION TO FETCH API
# -----------------------------

async def fetch_weather(city):

    # API URL
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        # requests.get() is blocking
        # asyncio.to_thread() runs it in a separate thread
        response = await asyncio.to_thread(
            requests.get,
            url,
            timeout=5  # Timeout after 5 seconds
        )

        # Convert JSON response to dictionary
        data = response.json()

        # Check if request successful
        if response.status_code == 200:

            # Create Pydantic object
            weather = WeatherData(
                city=data["name"],
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"],
                condition=data["weather"][0]["description"]
            )

            return weather

        else:
            print("Error fetching weather data.")
            print("Server Message:", data.get("message"))

            return None

    # Timeout error
    except requests.exceptions.Timeout:
        print("Request timed out.")

    # Any request-related error
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    return None

# -----------------------------
# MAIN ASYNC FUNCTION
# -----------------------------

async def main():

    # Ask user for city
    city = input("Enter city name: ")

    # Wait for async fetch function
    weather = await fetch_weather(city)

    # If data exists
    if weather:

        # Print weather report
        print("\nWeather Report")
        print(f"City: {weather.city}")
        print(f"Temperature: {weather.temperature}°C")
        print(f"Humidity: {weather.humidity}%")
        print(f"Condition: {weather.condition}")

        # Save data to JSON file
        with open("weather_data.json", "w") as file:
            json.dump(weather.model_dump(), file, indent=4)

        print("\nData saved to weather_data.json")

# -----------------------------
# RUN PROGRAM
# -----------------------------

# Start async program
asyncio.run(main())