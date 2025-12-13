from pathlib import Path

# Base directory of this package
BASE_DIR = Path(__file__).resolve().parent

# Project-level paths
DATA_ROOT = BASE_DIR.parent / "data"
INDEX_ROOT = BASE_DIR.parent / "indexes"

DOMAIN_INDEX_PATHS = {
    "artificial_intelligence": INDEX_ROOT / "artificial_intelligence",
    "medical": INDEX_ROOT / "medical",
    "climate": INDEX_ROOT / "climate",
    "cyber_security": INDEX_ROOT / "cyber_security",
    "business": INDEX_ROOT / "business",
    "psychology": INDEX_ROOT / "psychology",
    "automobile": INDEX_ROOT / "automobile",
}

DOMAIN_K = {
    "artificial_intelligence": 16,
    "medical": 12,
    "cyber_security": 14,
    "climate": 12,
    "business": 10,
    "psychology": 10,
    "automobile": 8,
}

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"
