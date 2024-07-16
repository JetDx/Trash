from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()

    # Load YOLO model
    #model = YOLO("yolov8n.pt")
    model = YOLO("preTaco.pt")
    model.to('cuda')

    # Train the model
    ##IF DATASET CHANGE, RENAME TO DATASETS
    results = model.train(data="datasets/data.yaml", epochs=100, imgsz=640, device="cuda")
    #results = model.train(resume=True)


