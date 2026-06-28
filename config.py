from pathlib import Path

# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
PDF_DIR = DATA_DIR / "pdfs"

CHROMA_DB_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "battery_collection"
# ==============================
# LLM
# ==============================

OLLAMA_MODEL = "llama3.2"

# ==============================
# Embedding Model
# ==============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==============================
# Chunking
# ==============================

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150