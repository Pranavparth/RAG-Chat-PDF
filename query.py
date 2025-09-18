from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# Initialize Pinecone client
pc = Pinecone(api_key="API_KEY", environment="ENVIRONMENT")

# Connect to your existing index
index_name = "Create an index via pinecone console"
index = pc.Index(index_name)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def search(query_text, top_k=3):
    # Convert query into embedding
    query_embedding = model.encode([query_text]).tolist()

    # Search Pinecone
    results = index.query(vector=query_embedding[0], top_k=top_k, include_metadata=True)

    return results
