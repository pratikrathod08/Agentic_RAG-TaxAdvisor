import os 
from typing import Literal
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from langchain_tavily import TavilySearch

from src import config 
from src.components.data_ingestion import DataIngestion
from src.utils.common_utils import get_llm
from src.state.graph_state import ValidationResponse

from src.tools.graph_tools import *
from src.state.graph_state import * 
from src.utils.common_utils import get_llm


def retrieve_node(state: AgentState):
    query = state["query"]
    context = vector_db_tool.invoke(query)

    return {
        "context": context
    }

def validate_node(state: AgentState):
    response = vector_search_validation_tool.invoke({"query": state['query'], "context": state['context']})

    return {
        "validation": response.validation
    }

def answer_node(state: AgentState):
    llm = get_llm(config.OPENAI_API_KEY)
    answer = llm.invoke(
        f"""
        Answer the question using ONLY the context below.

        Note : Answer should look like Tax Advisor. Adopt Tax Advisor Human persona for answer query.

        Question:
        {state['query']}

        Context:
        {state['context']}
        """
        )

    return {
        "answer": answer.content
    }

# def fallback_node(state: AgentState):
#     return {
#         "answer": "I do not have context for that. Please try websearch."
#     }

def fallback_node(state: AgentState):
    if state["validation"] == "no": 
        context = tavily_search_tool.invoke(state["query"] + "Provide context for india.")
        return {
        "context": context
    }

def route_after_validation(state: AgentState):
    if state["validation"] == "yes":
        return "answer"
    else:
        return "fallback"
    
