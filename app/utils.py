"""
Helper functions shared across the API.
"""

from app.mock_data import MOCK_DATABASE
from app.config import FALLBACK_EQUIPMENT_INFO

# Pre-build a lowercase-keyed version once at import time so every
# lookup doesn't have to rebuild the dict on every request.
_NORMALIZED_DATABASE = {name.strip().lower(): info for name, info in MOCK_DATABASE.items()}


def get_equipment_info(predicted_class: str) -> dict:
    """
    Look up equipment info by predicted class name.
    Matching is case-insensitive and trims whitespace, so it doesn't
    matter whether the model outputs "Lat Pull Down", "lat pull down",
    or "LAT PULL DOWN" — they all resolve to the same entry.
    """
    key = predicted_class.strip().lower()
    return _NORMALIZED_DATABASE.get(key, {**FALLBACK_EQUIPMENT_INFO, "equipment": predicted_class})


def list_all_equipment() -> list:
    """Return a list of every equipment name currently in the database."""
    return list(MOCK_DATABASE.keys())