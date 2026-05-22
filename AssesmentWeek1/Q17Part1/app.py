
import os
import json
import asyncio
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
API_KEY = os.getenv("API_KEY")
class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: int
    condition: str
async def fetch_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = await asyncio.to_thread(
            requests.get,
            url,
            timeout=5
        )
        data = response.json()
        if response.status_code == 200:
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

    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    return None
async def main():
    city = input("Enter city name: ")
    weather = await fetch_weather(city)
    if weather:
        print("\nWeather Report")
        print(f"City: {weather.city}")
        print(f"Temperature: {weather.temperature}°C")
        print(f"Humidity: {weather.humidity}%")
        print(f"Condition: {weather.condition}")
        with open("weather_data.json", "w") as file:
            json.dump(weather.model_dump(), file, indent=4)

        print("\nData saved to weather_data.json")
asyncio.run(main())