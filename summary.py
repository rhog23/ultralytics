from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules import Attention
from torchsummary import summary


summary(Attention(dim=128), input_size=(128, 32, 32), device="cpu")
