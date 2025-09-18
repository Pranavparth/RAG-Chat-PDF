# RAG-Chat-PDF 📄💬

A lightweight **Retrieval-Augmented Generation (RAG)** project that lets you **upload PDFs** and ask questions about them using **LLM embeddings + Pinecone vector DB + Streamlit frontend**.

---

## ⚡ Features
- Upload PDF documents 📚
- Extract and embed text using **Llama embeddings**
- Store embeddings in **Pinecone vector DB**
- Query stored documents and get context-aware answers
- Simple **Streamlit app** for interaction

---

## 🛠️ Tech Stack
- **Python 3.11**
- [Streamlit](https://streamlit.io/) – frontend
- [Pinecone](https://www.pinecone.io/) – vector database
- [PyPDF2](https://pypi.org/project/PyPDF2/) – PDF parsing
- [OpenAI / Llama Embeddings](https://platform.openai.com/) – embeddings

---

## 📂 Project Structure
RAG-Chat-PDF/
│── app.py # Streamlit frontend
│── embed.py # PDF ingestion & embedding
│── query.py # Query and retrieval logic
│── requirements.txt
│── README.md

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/RAG-Chat-PDF.git
cd RAG-Chat-PDF

2️⃣ Create virtual environment & install dependencies

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

📌 Usage
Upload a PDF document.
The system extracts, embeds, and stores text into Pinecone.
Enter your query in the chat UI.
Get context-aware answers instantly 🎯
🌟 Future Enhancements
Support multiple documents
Add chat history
Fine-tune embeddings
Deploy on cloud (Streamlit Cloud / HuggingFace Spaces)
