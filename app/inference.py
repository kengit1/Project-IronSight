"""
Model inference layer.

THIS IS THE ONLY FILE THE AI TEAM NEEDS TO EDIT.
Everything else in the backend (main.py, schemas, equipment lookup)
is already built against the contract defined by `predict()` below.

-----------------------------------------------------------------
INTEGRATION CONTRACT
-----------------------------------------------------------------
predict(image_bytes: bytes) -> Prediction

Where Prediction has:
    - class_name: str   -> must exactly match one of the 13 keys
                            in app/mock_data.py (case-insensitive
                            matching is handled for you in utils.py,
                            but the class list must match).
    - confidence: float -> a value between 0.0 and 1.0

-----------------------------------------------------------------
WHEN THE REAL MODEL IS READY:
-----------------------------------------------------------------
1. Load your YOLO/TensorFlow weights once, at module import time
   (not inside predict(), so it doesn't reload on every request).
2. Replace the body of predict() with a real call to your model.
3. Return a Prediction with the top class name + its confidence.
4. Leave everything else in the backend untouched — main.py already
   knows how to handle whatever predict() returns.

Example for a YOLOv8 classification model (uncomment and adapt):

    from ultralytics import YOLO
    import numpy as np
    import cv2

    _model = YOLO("weights/best.pt")  # loaded once at import

    def predict(image_bytes: bytes) -> "Prediction":
        np_arr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        results = _model(img)
        top = results[0].probs.top1
        confidence = float(results[0].probs.top1conf)
        class_name = _model.names[top]
        return Prediction(class_name=class_name, confidence=confidence)
"""

from dataclasses import dataclass


@dataclass
class Prediction:
    class_name: str
    confidence: float


def predict(image_bytes: bytes) -> Prediction:
    """
    MOCK IMPLEMENTATION — replace this function body once the real
    model is ready. Everything downstream (main.py) already expects
    exactly this return type, so no other file needs to change.
    """
    # Placeholder: always returns the same class with high confidence.
    # This lets the rest of the team build and test against a
    # predictable response while the real model is being trained.
    return Prediction(class_name="Lat Pull Down", confidence=0.94)