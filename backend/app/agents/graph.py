from langgraph.graph import StateGraph
from .planner_agent import generate_itinerary
from .weather_agent import fetch_weather

def build_trip_graph():
    graph = StateGraph()

    @graph.node
    def weather_node(state):
        return fetch_weather(state)

    @graph.node
    def plan_node(state):
        return generate_itinerary(state)

    # Order: fetch weather → generate itinerary
    graph.add_edge("weather_node", "plan_node")
    graph.set_entry_point("weather_node")
    graph.set_finish_point("plan_node")

    return graph.compile()
