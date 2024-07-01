import torch

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s") 

torch.cuda.is_available()

# Set device
device =torch.device('cuda')
print(f'Using device: {device}')

# !python train.py --img 640 --batch 16 --epochs 10 --data data.yaml --weights yolov5s.pt
