

"""
Pydantic models that define the exact shape of API responses.
FastAPI uses these to auto-generate accurate docs at /docs and to
validate that we always return well-formed data.
"""

from pydantic import BaseModel


class EquipmentInfo(BaseModel):
    equipment: str
    primary_muscle: str
    academic_info: str
    video_url: str


class PredictionResponse(BaseModel):
    status: str
    confidence: float
    data: EquipmentInfo


class LowConfidenceResponse(BaseModel):
    status: str
    message: str
    confidence: float


class HealthResponse(BaseModel):
    status: str