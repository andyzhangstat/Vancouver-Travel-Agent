from fastapi import APIRouter
from app.models.plan_request import PlanRequest
from app.models.plan_response import PlanResponse
from app.services.plan_service import create_plan

router = APIRouter()

@router.post("/plan", response_model=PlanResponse)
def plan_trip(req: PlanRequest):
    itinerary_json = create_plan(req)
    return PlanResponse(itinerary_json=itinerary_json)
