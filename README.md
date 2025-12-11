# Vancouver-Travel-Agent


This repository contains the backend for a **Vancouver Travel Planner AI**.  
The system generates personalized itineraries based on user preferences, dates, and weather conditions. It uses **GPT** for itinerary generation and integrates a **Weather API** to adjust recommendations. Multi-step workflows are orchestrated using **LangGraph**.

---

## Directory Structure

```
backend/
├── app/
│   ├── agents/
│   │   ├── planner_agent.py      # GPT-based itinerary generator
│   │   ├── weather_agent.py      # Fetches weather forecast
│   │   └── graph.py              # LangGraph workflow definition
│   ├── api/
│   │   └── routes_plan.py        # FastAPI routes
│   ├── models/
│   │   ├── plan_request.py       # Request schemas
│   │   └── plan_response.py      # Response schemas
│   ├── services/
│   │   ├── llm_service.py        # GPT API client
│   │   ├── weather_service.py    # Weather API client
│   │   └── plan_service.py       # Service layer connecting agents
│   ├── config.py                 # Configuration (API keys, settings)
│   └── main.py                   # FastAPI app entry
└── requirements.txt              # Python dependencies
```

---

## Features

1. **Intelligent Trip Planning**  
   - Generate multi-day itineraries with attractions, restaurants, and hotels.
   - Personalized based on user preferences.

2. **Weather-aware Itinerary**  
   - Fetches forecast for Vancouver.
   - GPT adapts daily recommendations based on weather.

3. **Multi-step Agent Workflow (LangGraph)**  
   - Weather fetch → GPT itinerary generation → optional budget/hotel steps.

4. **API Endpoints**  
   - `/api/plan` → Generate itinerary  
   - `/api/edit` → Edit existing itinerary (add/remove/update activities)

---

## Dependencies

- FastAPI
- Uvicorn
- Pydantic
- OpenAI GPT
- Requests
- LangGraph
- Python-dotenv

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the root directory:

```
GPT_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

- `GPT_API_KEY` → OpenAI API key (GPT-4/3.5)
- `WEATHER_API_KEY` → OpenWeatherMap API key

---

## Run the Backend

```bash
cd backend
uvicorn app.main:app --reload
```

API will be available at:

```
http://localhost:8000
```

---

## Example Request

**POST `/api/plan`**

```json
{
  "city": "Vancouver",
  "start_date": "2025-12-20",
  "end_date": "2025-12-25",
  "preferences": "nature, seafood, photography"
}
```

**Response (simplified)**

```json
{
  "itinerary_json": "{...JSON itinerary from GPT...}"
}
```

---

## Extending the System

- **Budget Agent**: calculate total cost based on hotels, attractions, and transport  
- **Hotel / Restaurant Agents**: integrate APIs for real-time recommendations  
- **PDF Export**: export itinerary to PDF for sharing  
- **Map Visualization**: add frontend map integration

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangGraph Documentation](https://github.com/langgraph/langgraph)
- [OpenAI GPT API](https://platform.openai.com/docs)
- [OpenWeatherMap API](https://openweathermap.org/api)

