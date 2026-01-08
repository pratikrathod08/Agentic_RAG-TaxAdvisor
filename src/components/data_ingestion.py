import os
from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from src import config

class DataIngestion: 
    def __init__(self, config): 
        self.doc_path = config.DOCS_PATH
        self.db_path = config.VECTORDB_PATH
        self.collection_name = config.COLLECTION_NAME
        self.embedding_model_name = config.EMBEDDING_MODEL_NAME
        self.text_splitter = RecursiveCharacterTextSplitter(
                                chunk_size=1000,
                                chunk_overlap=200
                            )
        
    def load_data(self): 
        files = os.listdir(self.doc_path)
        doc_paths = Path(self.doc_path)

        all_data = []

        for file in files: 
            full_file_path = os.path.join(doc_paths, file)
            loader = PyMuPDFLoader(full_file_path)
            data = loader.load()
            all_data.extend(data)

        return all_data
    
    def split_data(self, data): 
        chunks = self.text_splitter.split_documents(data)
        return chunks
    
    def get_embeddings_model(self): 
        embeddings = HuggingFaceEmbeddings(
            model_name=self.embedding_model_name
        )
        return embeddings
    
    def store_vectors(self, documents): 
        vector_store = Chroma(
                collection_name=self.collection_name,
                embedding_function=self.get_embeddings_model(),
                persist_directory=self.db_path,  
            )
        vector_store.add_documents(documents)

    def initialize_vector_storage(self): 
        print("Store vector initialized")

        data = self.load_data()
        print("data stored successfully")

        chunks = self.split_data(data)
        print("data splitted successfully")

        try: 
            self.store_vectors(chunks)
            print("Data stored to vectordb successfully!")
        except Exception as e: 
            print(f"Exception occure during data ingestion : {str(e)}")

    def get_retriever(self): 
        vector_store = Chroma(
                collection_name=self.collection_name,
                embedding_function=self.get_embeddings_model(),
                persist_directory=self.db_path,  
            )
        retriever = vector_store.as_retriever(
                        search_type="mmr", search_kwargs={"k": 3, "fetch_k": 5}
                    )
        return retriever
    

# if __name__ == "__main__": 
#     data_ingestion =    (config)
#     data_ingestion.initialize_vector_storage()

#     retriever = data_ingestion.get_retriever()
#     response = retriever.invoke("give me current rate of tax")
#     print(response)



        
    
        

    
    