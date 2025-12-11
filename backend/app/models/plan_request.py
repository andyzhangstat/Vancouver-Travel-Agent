from pydantic import BaseModel

class PlanRequest(BaseModel):
    city: str = "Vancouver"
    start_date: str  # Format: YYYY-MM-DD
    end_date: str    # Format: YYYY-MM-DD
    preferences: str = ""  # e.g., "nature, seafood, photography"
