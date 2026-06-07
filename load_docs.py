from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# -----------------------------
# 1. Load document
# -----------------------------
FILE_PATH = "data/my_document.txt"

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(f"File not found: {FILE_PATH}")

loader = TextLoader(FILE_PATH, encoding="utf-8")
documents = loader.load()

print(f"✅ Documents loaded: {len(documents)}")
print("📄 Sample content:\n", documents[0].page_content[:300])

# -----------------------------
# 2. Split into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

document_chunks = text_splitter.split_documents(documents)

print(f"✅ Chunks created: {len(document_chunks)}")

if len(document_chunks) == 0:
    raise ValueError("No chunks created. Check document content.")

# -----------------------------
# 3. Create embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# 4. Create FAISS vector store
# -----------------------------
vector_store = FAISS.from_documents(
    document_chunks,
    embeddings
)

# -----------------------------
# 5. Save FAISS index
# -----------------------------
FAISS_PATH = "faiss_index"
vector_store.save_local(FAISS_PATH)

print(f"✅ FAISS index saved at: {FAISS_PATH}")
print("🎉 Document indexing completed successfully!")