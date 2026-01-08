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


@tool(description="For vectordb search use this tool")
def vector_db_tool(query: str) -> str: 
    data_ingestion = DataIngestion(config)
    retriever = data_ingestion.get_retriever()
    context = retriever.invoke(query)
    # return f"Context retrieved by vectordb : {context} for query {query}"
    final_context = "\n\n".join(d.page_content for d in context)
    return final_context


@tool(description="validate retrieved context from vectordb")
def vector_search_validation_tool(context: str, query: str): 
    llm = get_llm(config.OPENAI_API_KEY)
    structured_llm = llm.with_structured_output(ValidationResponse)
    response = structured_llm.invoke(
        f"""
            Answer ONLY yes or no.

            Does the context answer the question?

            Question:
            {query}

            Context:
            {context}
            """
        )
    return response

@tool(description="Useful for websearch using tavily")
def tavily_search_tool(query: str): 
    tavily_search_tool = TavilySearch(
        max_results=5,
        topic="general",
        # include_answer=False,
        # include_raw_content=False,
        # include_images=False,
        # include_image_descriptions=False,
        # search_depth="basic",
        # time_range="day",
        # start_date=None,
        # end_date=None,
        # include_domains=None,
        # exclude_domains=None,
        # include_usage= False
    )
    search_result = tavily_search_tool.invoke(query)
    return search_result

if __name__ == "__main__":
    query = "what is gst?" 
    print(f"Query : {query}")

    context = vector_db_tool.invoke(query)
    print(f"Context : {context}")

    validation = vector_search_validation_tool.invoke({"query": query, "context": context})
    print(f"Validation : {validation}")

    search_result = tavily_search_tool.invoke(query)
    print(f"Tavily search context : {search_result}")
