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

   # activate model as dict with 2 models in it 
    ai_result = predict(uploaded_file=uploaded_file)

    # 
    if ai_result.get("error"):
        return {
            "status": "low_confidence",
            "message": "No equipment detected by any model. Image might not be clear.",
            "data": [config.FALLBACK_INFO] # خليناها List عشان الـ UI يتوقع دايماً List
        }

    valid_results = []
    
    # if there is results
    for res in ai_result.get("models_results", []):
        if res["confidence"] >= config.MIN_CONFIDENCE_THRESHOLD:
            # get the prediects of each 
            equipment_info = get_equipment_info(res["equipment_name"])
            
            # model with its prediction
            valid_results.append({
                "model_name": res["model"],
                "confidence": res["confidence"],
                "equipment_data": equipment_info
            })

    # 3. if all low conf
    if len(valid_results) == 0:
        return {
            "status": "low_confidence",
            "message": "Detected equipment with low confidence, try another image.",
            "data": [config.FALLBACK_INFO]
        }

    # 4. if ok
    return {
        "status": "success",
        "results": valid_results  
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