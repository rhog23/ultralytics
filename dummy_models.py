from ultralytics.nn.tasks import DetectionModel
from ultralytics import YOLO

det_model = DetectionModel(cfg="yolov8n-spd.yaml")
# det_model.info(detailed=True, verbose=True)


# model = YOLO("yolov8n-spd-old.yaml", task="detect")
# model.info(detailed=True, verbose=True)


# model.predict("WIN_20250115_15_12_32_Pro.jpg")