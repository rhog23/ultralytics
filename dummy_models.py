from ultralytics.nn.tasks import DetectionModel

det_model = DetectionModel(cfg="yolo11s-lightconv.yaml")
det_model.info(detailed=True, verbose=True)

# from ultralytics import YOLO

# model = YOLO("yolo11s.yaml", task="detect")
# model.info(detailed=True, verbose=True)
