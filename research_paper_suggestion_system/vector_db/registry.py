from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INDEX_ROOT = PROJECT_ROOT / "indexes"

DOMAIN_INDEX_PATHS = {
    "artificial_intelligence": INDEX_ROOT / "artificial_intelligence",
    "medical": INDEX_ROOT / "medical",
    "climate": INDEX_ROOT / "climate",
    "cyber_security": INDEX_ROOT / "cyber_security",
    "business": INDEX_ROOT / "business",
    "psychology": INDEX_ROOT / "psychology",
    "automobile": INDEX_ROOT / "automobile",
}