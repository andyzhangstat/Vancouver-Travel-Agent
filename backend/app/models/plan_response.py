from pydantic import BaseModel

class PlanResponse(BaseModel):
    itinerary_json: str  # The JSON string of the generated itinerary
