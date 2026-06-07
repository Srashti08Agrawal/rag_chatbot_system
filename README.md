# 🤖 RAG Chatbot System

A Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, FAISS, HuggingFace Embeddings, and Groq LLM. The chatbot answers user queries based on custom documents by retrieving relevant context and generating accurate responses.

---

## 🚀 Features

* Document-based Question Answering
* Retrieval-Augmented Generation (RAG)
* Semantic Search using FAISS Vector Store
* HuggingFace Embeddings
* Groq LLaMA 3 Integration
* FastAPI Backend
* Streamlit Frontend
* Context-Aware Responses
* Hallucination Reduction using Retrieved Context

---

## 🏗️ Project Architecture

User Query
↓
Streamlit UI
↓
FastAPI API
↓
LangChain RAG Pipeline
↓
FAISS Retriever
↓
Relevant Document Chunks
↓
Groq LLM (LLaMA 3)
↓
Generated Response

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python

### Frontend

* Streamlit

### LLM Framework

* LangChain

### Vector Database

* FAISS

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### Large Language Model

* LLaMA 3 70B (via Groq)

### Environment Management

* python-dotenv

---

## 📂 Project Structure

rag_chatbot_system/

├── main.py

├── endpoints.py

├── rag_chain.py

├── load_docs.py

├── ui.py

├── requirements.txt

├── .gitignore

├── .env

└── faiss_index/

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/Srashti08Agrawal/rag_chatbot_system.git

cd rag_chatbot_system

### Create Virtual Environment

python -m venv ragenv

### Activate Environment

Windows:

ragenv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key

---

## ▶️ Run Backend

uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

---

## ▶️ Run Frontend

streamlit run ui.py

---

## 📊 API Endpoint

### Ask Question

POST /ask

Request:

{
"question": "What is RAG?"
}

Response:

{
"answer": "Generated answer",
"confidence": "high",
"sources": []
}

---

## 🎯 Future Improvements

* Source citations
* Conversation memory
* Multi-document support
* Cloud deployment on AWS
* Authentication & Authorization
* Better confidence scoring

---

## 👩‍💻 Author

Srashti Agrawal

B.Tech CSE (AI & Data Science) - 2025

AKS University, Satna, Madhya Pradesh

GitHub: https://github.com/Srashti08Agrawal
