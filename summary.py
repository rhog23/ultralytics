from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.tasks import ClassificationModel
from ultralytics.nn.modules import Attention
from torchsummary import summary
from torchviz import make_dot
import torch


# summary(Attention(dim=128), input_size=(128, 32, 32), device="cpu")
summary(
    ClassificationModel("yolo11-cls-swint.yaml"),
    input_size=(3, 224, 224),
    device="cpu",
)



'''architecture visualization purpose'''
# model = ClassificationModel("yolo11n-cls-resnet18.yaml")
# sample_input = torch.randn(1, 3, 224, 224)
# output = model(sample_input)

# dot = make_dot(output, params=dict(list(model.named_parameters()) + [('input', sample_input)]))
# dot.format = 'png'
# dot.render('model')  # render the dot to a file named 'model.png' in th

