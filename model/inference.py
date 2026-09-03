from ultralytics import YOLO 
from PIL import Image
import os

# get the absolute path so the script can loock up into directly
CURRENT_DIR =  os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR , "best.pt")

model = YOLO(MODEL_PATH)

def predict(uploaded_file):
    # PIL library helps in creating an image from the path given 
    # old code used to work on a datatype the script could not dedce its type 
    # although it wotked
    img = Image.open(uploaded_file)
    results = model(img) 

    if len(results[0].boxes)>0 :
        box = results[0].boxes[0]
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])                
        # get the id 
        equipment_name = results[0].names[class_id]

        return {
            "equipment_name": equipment_name
            , "confidence": confidence ,
            "error" : None
        }
    return {
         "equipment_name": "Unknown"
        , "confidence": 0.0 ,
        "error" : "No Detection of equipment"
    }

# test 
#print(predict("seatRow.jpg"))