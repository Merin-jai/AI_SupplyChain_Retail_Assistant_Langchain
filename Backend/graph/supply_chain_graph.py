from langgraph.graph import StateGraph
from agents.demand_forecast import forecast_agent

def run_graph(user_input):
    graph = StateGraph()

    # Add forecast agent (others come later)
    graph.add_node("forecast", forecast_agent)

    # Since it's just one agent now
    graph.set_entry_point("forecast")
    graph.set_finish_point("forecast")

    app = graph.compile()
    return app.invoke(user_input)
