from ultralytics import YOLO
import time
import cv2
import matplotlib.pyplot as plt

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    results = model(frame)
    
    # Menggunakan matplotlib untuk menampilkan frame
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    # Mengakses hasil deteksi
    # Periksa dulu apakah results adalah list dan memiliki elemen
    if isinstance(results, list) and len(results) > 0:
        hasil_deteksi = results[0].xyxy  # Asumsi bahwa hasil pertama memiliki format yang diinginkan
        daftar_label = results[0].names
        
        count = 0
        for det in hasil_deteksi:
            label = daftar_label[int(det[5])]
            print(label)
            if int(det[5]) == 0:  # Misalnya, index 0 adalah 'person'
                count += 1
        print(count)
    
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()