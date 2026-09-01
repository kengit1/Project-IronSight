from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import config
from app.inference import predict
from app.utils import get_equipment_info, list_all_equipment
from app.schemas import PredictionResponse, LowConfidenceResponse, HealthResponse
from app.mock_data import MOCK_DATABASE

app = FastAPI(title="Gym Equipment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=HealthResponse)
def home():
    return {"status": "Backend Server is running!"}


@app.get("/equipment")
def get_all_equipment():
    """
    List every equipment class the API knows about.
    Useful for the frontend team to build UI without needing
    an image or the model to be ready.
    """
    return {"count": len(MOCK_DATABASE), "equipment": list_all_equipment()}


@app.get("/equipment/{name}")
def get_equipment_by_name(name: str):
    """
    Look up equipment info directly by name (case-insensitive),
    without going through image prediction. Handy for testing.
    """
    return get_equipment_info(name)


@app.post("/predict", response_model=PredictionResponse | LowConfidenceResponse)
async def predict_equipment(file: UploadFile = File(...)):
    # 1. Validate content type
    if not file.content_type or file.content_type not in config.ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{file.content_type}'. Please upload a JPEG, PNG, or WEBP image.",
        )

    # 2. Read image bytes
    image_bytes = await file.read()

    if len(image_bytes) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    if len(image_bytes) > config.MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size is {config.MAX_FILE_SIZE_MB}MB.",
        )

    # 3. Run inference (mock for now -- see app/inference.py)
    result = predict(image_bytes)

    # 4. Handle low-confidence predictions gracefully instead of
    #    confidently returning a possibly-wrong guess.
    if result.confidence < config.MIN_CONFIDENCE_THRESHOLD:
        return {
            "status": "low_confidence",
            "message": "Couldn't confidently identify this equipment. Try a clearer photo.",
            "confidence": result.confidence,
        }

    # 5. Look up equipment info for the predicted class
    equipment_info = get_equipment_info(result.class_name)

    return {
        "status": "success",
        "confidence": result.confidence,
        "data": equipment_info,
    }