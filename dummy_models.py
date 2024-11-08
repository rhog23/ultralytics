from ultralytics.nn.tasks import DetectionModel

det_model = DetectionModel(cfg="yolov10s-p2,4-ema.yaml")

# from ultralytics import YOLO

# model = YOLO("yolo11s.yaml", task="detect")
# model.info(detailed=True, verbose=True)
