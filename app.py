import streamlit as st
from embed import add_pdf_to_pinecone
from query import search
from llm import generate_answer

st.title("📄 PDF Q&A")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    num_chunks = add_pdf_to_pinecone(uploaded_file)
    st.success(f" Uploaded and stored {num_chunks} chunks in Pinecone!")

# Chat Section
query = st.text_input("Ask a question about your document:")
if query:
    matches = search(query, top_k=3)
    context = " ".join([m["metadata"]["text"] for m in matches])

    st.subheader("🔎 Retrieved Chunks")
    for m in matches:
        st.write(f"- {m['metadata']['text']} (score: {m['score']:.2f})")

    st.subheader(" Answer")
    answer = generate_answer(query, context)
    st.write(answer)
