from ultralytics.nn.tasks import DetectionModel

det_model = DetectionModel(cfg="yolo11s-p2,4.yaml")
# det_model.info()

# from ultralytics import YOLO

# model = YOLO("yolo11s.yaml", task="detect")
# model.info(detailed=True, verbose=True)
