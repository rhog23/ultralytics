from ultralytics.nn.tasks import DetectionModel

det_model = DetectionModel(cfg="yolo11-ghost-gam.yaml")

# from ultralytics import YOLO

# model = YOLO("yolo11s.yaml", task="detect")
# model.info(detailed=True, verbose=True)
