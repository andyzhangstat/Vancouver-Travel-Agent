from app.agents.graph import build_trip_graph
from app.models.plan_request import PlanRequest

trip_agent = build_trip_graph()

def create_plan(req: PlanRequest):
    state = {
        "city": req.city,
        "start_date": req.start_date,
        "end_date": req.end_date,
        "preferences": req.preferences
    }
    result_state = trip_agent.invoke(state)
    return result_state.get("itinerary", "{}")
