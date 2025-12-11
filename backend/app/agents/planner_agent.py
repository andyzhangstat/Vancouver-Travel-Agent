from app.services.llm_service import call_gpt

def generate_itinerary(state):
    """
    Generate a weather-aware itinerary using GPT.

    State contains:
    - city
    - start_date
    - end_date
    - preferences
    - weather_forecast (dict of date -> weather info)
    """
    city = state["city"]
    start_date = state["start_date"]
    end_date = state["end_date"]
    preferences = state.get("preferences", "")
    weather_forecast = state.get("weather_forecast", {})

    # Convert forecast dict to a readable string for GPT
    forecast_str = ""
    for date, info in weather_forecast.items():
        forecast_str += f"{date}: {info['condition']}, Max: {info['max_temp']}°C, Min: {info['min_temp']}°C\n"

    prompt = f"""
You are a Vancouver travel planning assistant.

The user will travel from {start_date} to {end_date} in {city}.
User preferences: {preferences}

Weather forecast for these dates:
{forecast_str}

Please generate a day-by-day itinerary, suggesting attractions, restaurants, and hotels.
- Prefer outdoor activities on sunny/clear days.
- Prefer indoor activities on rainy/cloudy days.
- Respond in JSON format:

{{
  "days": [
    {{
      "date": "...",
      "attractions": ["..."],
      "restaurants": ["..."],
      "hotel": "..."
    }}
  ],
  "total_days": ...,
  "notes": "..."
}}
"""

    itinerary_json = call_gpt(prompt)
    state["itinerary"] = itinerary_json
    return state
