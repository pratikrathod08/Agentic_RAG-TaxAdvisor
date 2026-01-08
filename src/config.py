import os, sys 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("MODEL_API_KEY")

langsmith_api_key = os.getenv("LANGSMITH_API_KEY")

DOCS_PATH = "./docs"
VECTORDB_PATH = "./chroma_db"

EMBEDDING_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
COLLECTION_NAME = "tax"