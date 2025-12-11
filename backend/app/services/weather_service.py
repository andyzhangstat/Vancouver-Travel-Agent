import requests
from app.config import settings

class WeatherService:
    BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

    @staticmethod
    def get_forecast(city: str, days: int = 5):
        """
        Fetch 5-day weather forecast for the given city using WeatherAPI.com
        Returns a dict: {date: condition, max_temp, min_temp}
        """
        params = {
            "key": settings.WEATHER_API_KEY,
            "q": city,
            "days": days,
            "aqi": "no",
            "alerts": "no"
        }
        try:
            resp = requests.get(WeatherService.BASE_URL, params=params, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"Weather API error: {e}")
            return {}

        data = resp.json()
        forecast = {}
        for day in data.get("forecast", {}).get("forecastday", []):
            date = day["date"]
            condition = day["day"]["condition"]["text"]
            max_temp = day["day"]["maxtemp_c"]
            min_temp = day["day"]["mintemp_c"]
            forecast[date] = {
                "condition": condition,
                "max_temp": max_temp,
                "min_temp": min_temp
            }

        return forecast
