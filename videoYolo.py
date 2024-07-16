import cv2
from ultralytics import YOLO
import time

# Load the YOLO model
model = YOLO("runs\\detect\\train4\\weights\\best.pt")

cap = cv2.VideoCapture(0) #Don't CHANGE THE NUMBER. JUST CHANGE UNPLUG THE CAMERA AND PLUG IT BACK IN.

def get_center(x1, y1, x2, y2):
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    return center_x, center_y

if not cap.isOpened():
    print("Error: Could not open video device.") #Unplug and replug camera. Its literally broken as dfuck. 
    exit()

frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image. You Idiot")
        break

    results = model(frame)
    print("Processing detection results:")
    if results is not None and hasattr(results[0], 'boxes'):
        boxes = results[0].boxes
        if boxes is not None and hasattr(boxes, 'xyxy'):
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                conf = box.conf[0].cpu().numpy()
                cls = box.cls[0].cpu().numpy()
                center_x, center_y = get_center(x1, y1, x2, y2)
                class_name = results[0].names[int(cls)] #Finally got it to work
                print(f"Class: {class_name}, Confidence: {conf:.2f}, BBox: ({x1}, {y1}), ({x2}, {y2}), Center: ({center_x}, {center_y})")
                #I don't fucking understand this
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            print("No bounding boxes found in the results.")
    else:
        print("No bounding boxes found in the results.")

    #To not clog up the machine.
    current_time = time.time()
    if current_time - start_time >= 10:
        output_path = f"screenshots/frame_{frame_count:04d}.jpg"
        cv2.imwrite(output_path, frame)
        frame_count += 1
        start_time = current_time  # Reset the timer

    cv2.imshow('YOLO Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        break

cap.release()
cv2.destroyAllWindows()
