
from app.services.weather_service import WeatherService

def fetch_weather(state):
    """
    Fetch 5-day forecast for the trip city and store in the state
    """
    city = state.get("city", "Vancouver")
    forecast = WeatherService.get_forecast(city)
    state["weather_forecast"] = forecast
    return state
