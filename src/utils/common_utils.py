import os 
from src import config

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
load_dotenv()



def get_llm(api_key): 
    llm = ChatOpenAI(api_key=api_key, model_name="gpt-5", temperature=0.1)
    return llm

# if __name__ == "__main__": 
#     llm = get_llm(config.OPENAI_API_KEY)
#     response = llm.invoke("how can you help me ")
#     print(response)