from fastapi import FastAPI
from pydantic import BaseModel
from rag_chain import init_rag
from endpoints import router as rag_router

app = FastAPI()

# -----------------------------
# Response schema
# -----------------------------
class HealthResponse(BaseModel):
    status: str


# -----------------------------
# Startup
# -----------------------------
@app.on_event("startup")
def startup_event():
    init_rag()


# -----------------------------
# Health check
# -----------------------------
@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "RAG API running"}


# -----------------------------
# Include RAG routes
# -----------------------------
app.include_router(rag_router)