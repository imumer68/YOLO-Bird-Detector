from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

result = model.predict(source='path/to/images', epochs=2, show=True, save=True)

