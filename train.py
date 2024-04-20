from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

result = model.train(data='config.yaml', epochs=25, show=True, save=True)

