from fastapi import FastAPI 
from pydantic import BaseModel

from src.components.data_ingestion import DataIngestion
from src.components.graph import Graph
from src import config

app = FastAPI()

class AskRequest(BaseModel):
    query: str


class AskResponse(BaseModel):
    answer: str

@app.get("/health")
def health(): 
    return {"Response": "API's working"}

@app.get("/create_vectors")
def indexing(): 
    data_ingestion = DataIngestion(config=config)
    try: 
        data_ingestion.initialize_vector_storage()
        return {"Response": "Vector storage created successfully!"}
    except Exception as e: 
        return {'Response': f"Error occure during vector storage creation. -- Error : {str(e)}"}
    
@app.post("/ask", response_model=AskResponse)
def query(request: AskRequest): 
    try: 
        graph = Graph()
        agent = graph.get_graph()
        result = agent.invoke({"query": request.query})
        return {
                "answer": result.get("answer", "No answer generated")
            }
    except Exception as e: 
        return {
            "answer": f"Error occurred while processing query: {str(e)}"
        }