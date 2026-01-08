import os

from langgraph.graph import StateGraph, END

from src.tools.graph_tools import *
from src.state.graph_state import * 
from src.nodes.graph_nodes import *

class Graph:
    def __init__(self): 
        pass 

    def get_graph(self): 
        graph = StateGraph(AgentState)

        graph.add_node("retrieve", retrieve_node)
        graph.add_node("validate", validate_node)
        graph.add_node("answer", answer_node)
        graph.add_node("fallback", fallback_node)

        graph.set_entry_point("retrieve")
        graph.add_edge("retrieve", "validate")

        graph.add_conditional_edges(
            "validate",
            route_after_validation
        )

        graph.add_edge("fallback", "answer")
        graph.add_edge("answer", END)

        rag_agent = graph.compile()

        return rag_agent
    

# if __name__ == "__main__": 
#     query = "what is gst?"
#     graph = Graph().get_graph()
#     result = graph.invoke({
#     "query": query
# })
#     print("Full Result : ", result)
#     print("*"*50)
#     print(f"Final Answer : {result['answer']}")

