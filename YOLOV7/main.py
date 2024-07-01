import torch

torch.cuda.is_available()

# Set device
device =torch.device('cuda')
print(f'Using device: {device}')

# python train.py --device 0 --batch 2 --epoch 10 --data data/data.yaml --img 640 --cfg cfg/training/yolov7.yaml --weights yolov7.pt --hyp data/hyp.scratch.p5.yaml