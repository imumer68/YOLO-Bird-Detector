from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

# result = model.train(data='config.yaml', epochs=1, show=True, save=True)
# result = model.val(data='config.yaml', epochs=1, show=True, save=True)
# result = model.predict(source='D:/Python Stuff/Datasets/Mouse/test/images', epochs=2, show=True, save=True)

