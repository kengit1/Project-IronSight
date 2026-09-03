from model import (config , utils , inference)
from model.utils import get_equipment_info
from model.inference import predict

def process_upload(uploaded_file):
    # Init Tests
    if not config.is_valid_image(uploaded_file.name):
        return {
            "status": "error"
            , "message": "not supported , only : JPG, PNG, WEBP, JPEG."
        }
        
    if not config.is_valid_size(uploaded_file.size):
        return {
            "status": "error"
            , "message": f"Image above the standard size :{config.MAX_FILE_SIZE_MB}"
        }

    # activate model
    ai_result = predict(uploaded_file= uploaded_file)

    # aggregate data 
    if ai_result["error"] or ai_result["confidence"] < config.MIN_CONFIDENCE_THRESHOLD:
        return {
            "status": "low_confidence",
            "message": "Image not clear , try another one",
            "confidence" : ai_result["confidence"] ,
            "data": config.FALLBACK_INFO
        }

    # get actual data
    equipment_info = get_equipment_info(ai_result["equipment_name"])

    return {
        "status": "success",
        "confidence": ai_result["confidence"],
        "data": equipment_info
    }

# test
import os
# rubber class to test a streamlit-like uploaded file 
# the uploaded file will be an image stored in ram , so that is_valid_imag can access its size 
# 
'''
class DummyStreamlitFile:
    def __init__(self, file_path):
        self.name = os.path.basename(file_path)
        self.size = os.path.getsize(file_path)
        self.file_path = file_path
        
    def read(self):
        # a PIL function to load from ram 
        with open(self.file_path, "rb") as f:
            return f.read()

# actual test 
test_file = DummyStreamlitFile("test.webp")
print(process_upload(test_file))
'''