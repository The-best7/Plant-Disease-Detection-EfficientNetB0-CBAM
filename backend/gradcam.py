# c:\Users\Kartik\Downloads\ntcc\plant-disease-app\backend\gradcam.py

import cv2
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image

class GradCAM:
    """
    Grad-CAM++ implementation for PyTorch.
    Hooks onto the specified target layer to calculate saliency maps.
    """
    def __init__(self, model, target_layer, device='cpu'):
        self.model = model
        self.target_layer = target_layer
        self.device = device
        self.gradients = None
        self.activations = None
        self.hook_handles = []
        self._register_hooks()

    def _register_hooks(self):
        def fwd_hook(module, inp, out):
            self.activations = out.detach()
        def bwd_hook(module, grad_in, grad_out):
            self.gradients = grad_out[0].detach()
            
        h1 = self.target_layer.register_forward_hook(fwd_hook)
        h2 = self.target_layer.register_full_backward_hook(bwd_hook)
        self.hook_handles.extend([h1, h2])

    def generate(self, img_tensor, class_idx=None):
        self.model.eval()
        # Ensure tensor is on correct device and has batch dim
        if img_tensor.dim() == 3:
            img_tensor = img_tensor.unsqueeze(0)
            
        img_tensor = img_tensor.to(self.device).requires_grad_(True)
        logits = self.model(img_tensor)
        
        if class_idx is None:
            class_idx = logits.argmax(dim=1).item()
            
        self.model.zero_grad()
        logits[0, class_idx].backward()

        # Pool gradients across channels
        grads = self.gradients
        if grads is None or self.activations is None:
            # Fallback if hook wasn't triggered
            return np.zeros((img_tensor.shape[2], img_tensor.shape[3])), class_idx
            
        alpha_num = grads.pow(2)
        alpha_denom = (2 * grads.pow(2) + torch.sum(self.activations * grads.pow(3), dim=(2, 3), keepdim=True))
        alpha_denom = torch.where(alpha_denom != 0, alpha_denom, torch.ones_like(alpha_denom))
        alphas = alpha_num / (alpha_denom + 1e-7)
        positive_grads = F.relu(grads)
        weights = torch.sum(alphas * positive_grads, dim=(2, 3), keepdim=True)
        
        cam = (weights * self.activations).sum(dim=1).squeeze(0)  # [H, W]
        cam = F.relu(cam)
        cam = cam - cam.min()
        cam = cam / (cam.max() + 1e-8)
        cam = cam ** 1.3
        return cam.cpu().numpy(), class_idx

    def release_hooks(self):
        """Release PyTorch hooks to avoid memory leaks."""
        for handle in self.hook_handles:
            handle.remove()
        self.hook_handles = []

def overlay_cam(pil_img, cam, alpha=0.25, img_size=224):
    """
    Overlay Grad-CAM heatmap on leaf.
    Uses HSV color masking to restrict the heatmap overlay to actual leaf tissues (ignoring backgrounds).
    """
    # Resize original image
    img_np = np.array(pil_img.resize((img_size, img_size), Image.LANCZOS))
    
    # Resize and filter heatmap
    cam_up = cv2.resize(cam, (img_size, img_size), interpolation=cv2.INTER_CUBIC)
    cam_up = cv2.GaussianBlur(cam_up, (5, 5), 0)
    cam_up = cv2.normalize(cam_up, None, 0, 1, cv2.NORM_MINMAX)
    cam_up = np.power(cam_up, 1.35)
    
    # Apply HSV green/yellow leaf color mask
    hsv = cv2.cvtColor(img_np, cv2.COLOR_RGB2HSV)
    # Mask to isolate green/yellow leaf shades (hue: 15 to 120)
    mask = cv2.inRange(hsv, (15, 20, 20), (120, 255, 255))
    mask = mask.astype(np.float32) / 255.0
    
    # Close small gaps in the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Apply leaf mask to activation map
    cam_up = cam_up * mask
    cam_up = cv2.medianBlur((cam_up * 255).astype(np.uint8), 5).astype(np.float32) / 255.0
    
    # Generate Turbo color-mapped heatmap
    heatmap = cv2.applyColorMap(np.uint8(cam_up * 255), cv2.COLORMAP_TURBO)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    
    # Blend image and heatmap
    overlay = cv2.addWeighted(img_np, 1 - alpha, heatmap, alpha, 0)
    
    # Bounding box / disease localization analysis
    # Find contours where attention is high (e.g. > 50% max activation)
    high_att_mask = (cam_up > 0.5).astype(np.uint8) * 255
    contours, _ = cv2.findContours(high_att_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    localization_info = "The model focused on diffuse areas of the leaf surface."
    if contours:
        # Find largest contour
        largest_cnt = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_cnt)
        # Determine location
        loc_y = "middle" if 0.33 <= (y + h/2)/img_size <= 0.66 else ("top" if (y + h/2)/img_size < 0.33 else "bottom")
        loc_x = "center" if 0.33 <= (x + w/2)/img_size <= 0.66 else ("left" if (x + w/2)/img_size < 0.33 else "right")
        localization_info = f"The model focused on the {loc_y}-{loc_x} section of the leaf, identifying characteristic localized patterns."
        
    return img_np, heatmap, overlay, localization_info
