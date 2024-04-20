from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

result = model.val(data='config.yaml', epochs=5, show=True, save=True)

