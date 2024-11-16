from ultralytics.nn.tasks import DetectionModel

det_model = DetectionModel(cfg="yolo11m-p2.yaml")
det_model = DetectionModel(cfg="yolo11l-p2.yaml")
det_model = DetectionModel(cfg="yolo11x-p2.yaml")
# det_model.info()

# from ultralytics import YOLO

# model = YOLO("yolo11s.yaml", task="detect")
# model.info(detailed=True, verbose=True)
