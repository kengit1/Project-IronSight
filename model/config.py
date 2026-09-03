MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "webp"]
MIN_CONFIDENCE_THRESHOLD = 0.40

FALLBACK_INFO = {
    "equipment": "Unknown",
    "primary_muscle": "Unknown",
    "academic_info": "No academic data available.",
    "video_url": "https://musclewiki.com",
}

def is_valid_image(filename):
    # inliner , get what after the '.' then lower 
    # - means include also '.' at splitting
    ext = filename.split(".")[-1].lower()
    return ext in ALLOWED_EXTENSIONS

def is_valid_size(file_size_bytes):
    size_mb = file_size_bytes / (1024 * 1024)
    return size_mb <= MAX_FILE_SIZE_MB