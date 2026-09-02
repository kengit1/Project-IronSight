

from dataclasses import dataclass
import tempfile
import os
from ultralytics import YOLO

# Load the model once at import time (not inside predict(), so it
# doesn't reload on every request). Path is relative to this file's
# location, so it works on any machine regardless of who runs it.
_MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "best.pt")
_model = YOLO(_MODEL_PATH)


@dataclass
class Prediction:
    class_name: str
    confidence: float


def predict(image_bytes: bytes) -> Prediction:
    # The model expects a file path, but we receive raw image bytes
    # from the upload -- so we write them to a temporary file first.
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp.write(image_bytes)
        tmp_path = tmp.name

    try:
        results = _model(tmp_path)

        if len(results[0].boxes) > 0:
            box = results[0].boxes[0]
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            equipment_name = results[0].names[class_id]
            return Prediction(class_name=equipment_name, confidence=confidence)
        else:
            # No equipment detected -- return 0 confidence so main.py's
            # existing low-confidence handling kicks in automatically.
            return Prediction(class_name="Unknown", confidence=0.0)
    finally:
        os.remove(tmp_path)  # clean up the temp file either way