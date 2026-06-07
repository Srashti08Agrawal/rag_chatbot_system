import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

# -----------------------------
# Globals
# -----------------------------
_embeddings = None
_qa_chain = None
_retriever = None


# -----------------------------
# Initialize RAG
# -----------------------------
def init_rag():
    global _embeddings, _qa_chain, _retriever

    if _qa_chain is not None:
        return

    print("🔹 Initializing RAG (Groq + FAISS)...")

    # Embeddings
    _embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS index
    vector_store = FAISS.load_local(
        "faiss_index",
        _embeddings,
        allow_dangerous_deserialization=True
    )

    _retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Groq LLM
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama3-70b-8192",
        temperature=0.1
    )

    # Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Answer the question strictly using the provided context.
If the context does not contain the answer, respond exactly with:
"I don't know based on the provided information."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # LCEL Chain (LangChain v1+ safe)
    _qa_chain = (
        {
            "context": _retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )


# -----------------------------
# Ask RAG
# -----------------------------
async def ask_rag(question: str):
    init_rag()

    answer = _qa_chain.invoke(question).strip()

    if not answer or len(answer) < 5:
        return {
            "answer": "I don't know based on the provided information.",
            "sources": []
        }

    return {
        "answer": answer,
        "sources": []   # intentionally hidden for GPT-like UI
    }