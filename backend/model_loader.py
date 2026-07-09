# c:\Users\Kartik\Downloads\ntcc\plant-disease-app\backend\model_loader.py

import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import timm

class ChannelAttention(nn.Module):
    def __init__(self, channels, reduction=16):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
        self.fc = nn.Sequential(
            nn.Conv2d(channels, channels // reduction, 1, bias=False),
            nn.ReLU(inplace=True),
            nn.Conv2d(channels // reduction, channels, 1, bias=False)
        )
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc(self.avg_pool(x))
        max_out = self.fc(self.max_pool(x))
        return self.sigmoid(avg_out + max_out)

class SpatialAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(2, 1, kernel_size=7, padding=3, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = torch.cat([avg_out, max_out], dim=1)
        return self.sigmoid(self.conv(x))

class CBAM(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.ca = ChannelAttention(channels)
        self.sa = SpatialAttention()

    def forward(self, x):
        x = self.ca(x) * x
        x = self.sa(x) * x
        return x

class PlantEfficientNetCBAM(nn.Module):
    def __init__(self, num_classes=38):
        super().__init__()
        # Pretrained=False since we load our own weights
        self.backbone = timm.create_model("efficientnet_b0", pretrained=False, num_classes=0, global_pool="")
        feature_dim = self.backbone.num_features
        self.cbam = CBAM(feature_dim)
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Sequential(
            nn.Linear(feature_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.backbone.forward_features(x)
        x = self.cbam(x)
        x = self.pool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

    def get_cam_layer(self):
        # We can use the blocks[-3] or conv_head for Grad-CAM
        # The notebook used: cbam_model.backbone.blocks[-3] for GradCAM target
        return self.backbone.blocks[-3]

def load_model(weights_path: str, num_classes: int = 38, device: str = 'cpu') -> nn.Module:
    """Instantiate and load the trained model weights."""
    model = PlantEfficientNetCBAM(num_classes=num_classes)
    if not os.path.exists(weights_path):
        raise FileNotFoundError(f"Model weights file not found at: {weights_path}")
    
    checkpoint = torch.load(weights_path, map_location=device)
    if isinstance(checkpoint, dict) and 'state' in checkpoint:
        state_dict = checkpoint['state']
    else:
        state_dict = checkpoint
        
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return model
