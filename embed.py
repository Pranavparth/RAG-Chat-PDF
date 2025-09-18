from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import PyPDF2

# Initialize Pinecone client
pc = Pinecone(api_key="API_KEY", environment="ENVIRONMENT")

# Connect to your existing index
index_name = "Create an index via pinecone console"
index = pc.Index(index_name)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def add_pdf_to_pinecone(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = model.encode(chunks).tolist()

    vectors = [
        {"id": f"chunk-{i}", "values": emb, "metadata": {"text": chunks[i]}}
        for i, emb in enumerate(embeddings)
    ]

    index.upsert(vectors=vectors)
    return f"Uploaded {len(chunks)} chunks to Pinecone!"
