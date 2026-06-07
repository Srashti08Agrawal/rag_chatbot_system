from fastapi import APIRouter
from pydantic import BaseModel
from rag_chain import ask_rag

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

class RAGResponse(BaseModel):
    answer: str
    confidence: str
    sources: list

@router.post("/ask", response_model=RAGResponse)
async def ask_question(request: QuestionRequest):
    result = await ask_rag(request.question)

    answer = result["answer"]
    sources = result.get("sources", [])

    confidence = "low" if "I don't know" in answer else "high"

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": sources
    }