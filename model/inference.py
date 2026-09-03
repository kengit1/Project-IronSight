from ultralytics import YOLO 
from PIL import Image
import os

# get the absolute path so the script can loock up into directly
CURRENT_DIR =  os.path.dirname(os.path.abspath(__file__))
MODEL_PATH_v1 = os.path.join(CURRENT_DIR , "best.pt")
MODEL_PATH_v2 = os.path.join(CURRENT_DIR , "best_v2.pt")

model_v1 = YOLO(MODEL_PATH_v1)
model_v2 = YOLO(MODEL_PATH_v2)

def predict(uploaded_file):
    # PIL library helps in creating an image from the path given 
    # old code used to work on a datatype the script could not dedce its type 
    # although it wotked
    img = Image.open(uploaded_file)
    results_v1 = model_v1(img)
    results_v2 = model_v2(img) 

    response = {"models_results": [], "error": None}

    # 
    if len(results_v1[0].boxes) > 0:
        box_v1 = results_v1[0].boxes[0]
        response["models_results"].append({
            "equipment_name": results_v1[0].names[int(box_v1.cls[0])],
            "confidence": float(box_v1.conf[0]),
            "model": "v1"
        })

    # 
    if len(results_v2[0].boxes) > 0:
        box_v2 = results_v2[0].boxes[0]
        response["models_results"].append({
            "equipment_name": results_v2[0].names[int(box_v2.cls[0])],
            "confidence": float(box_v2.conf[0]),
            "model": "v2"
        })

    # التعامل مع حالة الفشل التام للموديلين
    if not response["models_results"]:
        return {
            "models_results": [],
            "error": "No Detection of equipment"
        }
        
    return response

# test 
#print(predict("seatRow.jpg"))