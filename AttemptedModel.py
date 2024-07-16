import cv2
from ultralytics import YOLO

model = YOLO("runs\\detect\\train4\\weights\\best.pt")  

# Initialize the camera (0 is usually the default camera, change if you have multiple cameras)
cap = cv2.VideoCapture(0)

def get_center(x1, y1, x2, y2):
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    return center_x, center_y
        
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image. You Idiot")
        break

    results = model(frame)
    #print(results)
    #print("Type:" + str(type(results)))
    #print("Results:" + str(results))


        # Process results?????/
    print("Processing detection results:")
    if results is not None and hasattr(results, 'boxes'):
        boxes = results.boxes
        if boxes is not None and hasattr(boxes, 'xyxy'):
            for box in boxes.xyxy:
                x1, y1, x2, y2 = box[:4]
                conf = box[4]
                cls = box[5]
                center_x, center_y = get_center(x1, y1, x2, y2)
                class_name = results.names[int(cls)]
                print(f"Class: {class_name}, Confidence: {conf:.2f}, BBox: ({x1}, {y1}), ({x2}, {y2}), Center: ({center_x}, {center_y})")
    else:
        print("No bounding boxes found in the results asshole.")


    cv2.imshow('YOLO Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        break

cap.release()
cv2.destroyAllWindows()
