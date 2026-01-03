# Agentic_RAG_Demo
Demo project for agentic rag.

### Step 1 : Github Repository Creation 

### Step 2 : Create environment file

### Step 3 : Create Requirements.txt file. 

### Step 4 : Create Setup File

### Step 5 : Create Virtual Environment

`using uv`
```bash 
uv --version
uv venv .venv
uv pip install -r requirements.txt
uv pip list  
```

- Run command in terminal to run inside environment.

```bash
.venv\scripts\activate
```
### Step 6 : Add venv and .env to .gitignore

### Step 7 : Create basic folder structure

### Step 8 : Import fastapi in main file and create health route for check api's working and packages installed properly. 

```bash 
uvicorn src.main:app --reload
```

### Step 9 : push basic folder structure to github
