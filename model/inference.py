from ultralytics import YOLO
import json

# get the weight
model = YOLO("S:/MyWork/AI_Projects/Project_IronSight/Project-IronSight/model/best.pt")

def detect_equipment(image_path):
    # run the inference
    results = model(image_path)
    
    # extract the result from the image
    if len(results[0].boxes) > 0:
        # take the hieghst box value
        box = results[0].boxes[0]
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        
        # get the id 
        equipment_name = results[0].names[class_id]
        
        # data contract
        response = {
            "equipment_name": equipment_name,
            "confidence": round(confidence, 2),
            "error": None
        }
    else:
        response = {
            "equipment_name": None,
            "confidence": 0.0,
            "error": "No Equipment were detected in the Image"
        }
        
    return json.dumps(response, ensure_ascii=False)

# 
print(detect_equipment("S:/MyWork/AI_Projects/Project_IronSight/Project-IronSight/model/test_image.webp"))