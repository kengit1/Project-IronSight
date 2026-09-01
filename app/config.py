"""
Central place for all configurable values.
Change these here instead of hunting through main.py.
"""

# --- Upload limits ---
MAX_FILE_SIZE_MB = 10
ALLOWED_CONTENT_TYPES = ("image/jpeg", "image/png", "image/jpg", "image/webp")

# --- Model confidence handling ---
# If the model's confidence for its top prediction is below this,
# we treat it as "not confident enough" instead of returning a guess.
# Ask the AI team what a reasonable threshold is once real accuracy numbers exist.
MIN_CONFIDENCE_THRESHOLD = 0.40

# --- CORS ---
# Replace "*" with your actual Streamlit/Flutter origin(s) before the demo.
ALLOWED_ORIGINS = ["*"]

# --- Fallback equipment info ---
# Used when a predicted class isn't found in the equipment database
# (shouldn't happen once class names are locked, but guards against typos/mismatches).
FALLBACK_EQUIPMENT_INFO = {
    "equipment": "Unknown",
    "primary_muscle": "Unknown",
    "academic_info": "No academic data available for this equipment yet.",
    "video_url": "https://musclewiki.com",
}