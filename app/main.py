import os
import requests


API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Paris"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

if not API_KEY:
    raise ValueError(
        "WEATHER_API_KEY not found in environment variables!"
    )


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "lang": "en",
        "aqi": "no"
    }
    response = requests.get(WEATHER_API_URL, params=params)
    response.raise_for_status()

    data = response.json()
    print(
        f"Weather in {CITY}: {data['current']['temp_c']}°C, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
