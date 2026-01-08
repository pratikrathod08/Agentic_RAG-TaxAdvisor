# Agentic_RAG
Demo project for agentic rag.

#### Step 1 : Github Repository Creation 

#### Step 2 : Create environment file

#### Step 3 : Create Requirements.txt file. 

#### Step 4 : Create Setup File

#### Step 5 : Create Virtual Environment

`using uv`
```bash 
uv --version
uv venv .venv
uv pip install -r requirements.txt
uv pip list  

- Run file command
uv run python -m src.components.data_ingestion
```

- Run command in terminal to run inside environment.

```bash
.venv\scripts\activate
```
#### Step 6 : Add venv and .env to .gitignore

#### Step 7 : Create basic folder structure

#### Step 8 : Import fastapi in main file and create health route for check api's working and packages installed properly. 

```bash 
uvicorn src.main:app --reload
```

#### Step 9 : push basic folder structure to github

#### Step 10 : Create notebook folder and start creatinng components. 

- Create Required functions 
1. Read pdf files. 
2. Apply embeddings on text.  
3. Store in vectordb. 
4. Create Retriever 

- Create data ingestion component. 

5. create function for get llm model. 

- Create vectordb tool for RAG.
- Create validation tool for validate retrieved context.
- Create websearch tool for fallback. 

6. Create graph using langgraph. 

- Create state
- Create nodes for each function and conditions. 
- Create Graph. 
- Test with questions. 

#### Step 11 : Create structure for graph. 

- Create tools forlder and store all tools inside. 
- Create state folder to store schemas. 
- Create nodes folder to store all nodes. 
- Create Graph component for create graph.


