# c:\Users\Kartik\Downloads\ntcc\plant-disease-app\backend\predict.py

import os
import uuid
import torch
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from backend.model_loader import load_model
from backend.gradcam import GradCAM, overlay_cam
from backend.disease_database import DISEASE_DB

# Core settings
IMG_SIZE = 224
MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]

# Validation transform identical to the training notebook
valid_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop(IMG_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(MEAN, STD),
])

# Exact class names in alphabetical order (how PyTorch's ImageFolder loads them)
CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

class Predictor:
    def __init__(self, weights_path: str, static_dir: str):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Loading inference model on device: {self.device}")
        
        # Load winning model (EfficientNet-B0 + CBAM)
        self.model = load_model(weights_path, num_classes=len(CLASS_NAMES), device=self.device)
        self.model.eval()
        
        # Instantiate Grad-CAM++ with the target layer blocks[-3]
        target_layer = self.model.get_cam_layer()
        self.grad_cam = GradCAM(self.model, target_layer, device=self.device)
        
        self.static_dir = static_dir
        self.uploads_dir = os.path.join(static_dir, 'uploads')
        self.heatmaps_dir = os.path.join(static_dir, 'heatmaps')
        
        # Ensure static subdirectories exist
        os.makedirs(self.uploads_dir, exist_ok=True)
        os.makedirs(self.heatmaps_dir, exist_ok=True)

    def predict(self, pil_image: Image.Image):
        # 1. Preprocess and run inference
        input_tensor = valid_transform(pil_image).to(self.device)
        
        # We need the gradient hook active for Grad-CAM, so do not use torch.no_grad()
        # but do set model to eval mode (already done)
        input_tensor_with_grad = input_tensor.clone().unsqueeze(0).requires_grad_(True)
        
        # Forward pass
        logits = self.model(input_tensor_with_grad)
        probs = torch.softmax(logits, dim=1)[0]
        
        # Retrieve prediction
        pred_idx = probs.argmax().item()
        confidence = probs[pred_idx].item()
        class_name = CLASS_NAMES[pred_idx]
        
        # 2. Run Grad-CAM++
        cam_map, _ = self.grad_cam.generate(input_tensor, class_idx=pred_idx)
        
        # Overlay heatmap on original image (which extracts the leaf HSV mask)
        orig_np, heatmap_np, overlay_np, localization_text = overlay_cam(pil_image, cam_map, alpha=0.35, img_size=IMG_SIZE)
        
        # 3. Save images to static folders with a unique ID
        request_id = str(uuid.uuid4())
        
        orig_filename = f"orig_{request_id}.jpg"
        heatmap_filename = f"hmap_{request_id}.jpg"
        overlay_filename = f"over_{request_id}.jpg"
        
        orig_path = os.path.join(self.uploads_dir, orig_filename)
        heatmap_path = os.path.join(self.heatmaps_dir, heatmap_filename)
        overlay_path = os.path.join(self.heatmaps_dir, overlay_filename)
        
        # Save as JPEG
        Image.fromarray(orig_np).save(orig_path, "JPEG")
        Image.fromarray(heatmap_np).save(heatmap_path, "JPEG")
        Image.fromarray(overlay_np).save(overlay_path, "JPEG")
        
        # 4. Fetch details from database
        db_entry = DISEASE_DB.get(class_name, {
            "plant_name": class_name.split("___")[0].replace("_", " "),
            "disease_name": class_name.split("___")[-1].replace("_", " "),
            "status": "Unknown",
            "description": "Information not available.",
            "symptoms": [],
            "causes": [],
            "prevention": [],
            "organic_remedies": [],
            "chemical_remedies": [],
            "management_practices": "N/A"
        })
        
        # 5. Severity Estimation based on attention density (heuristic)
        # We look at the percentage of leaf area where Grad-CAM attention is high
        high_activation_ratio = np.sum(cam_map > 0.4) / cam_map.size
        if db_entry["status"] == "Healthy":
            severity = "Healthy"
        elif high_activation_ratio < 0.15:
            severity = "Mild"
        elif high_activation_ratio < 0.35:
            severity = "Moderate"
        else:
            severity = "Severe"
            
        # Explanatory text builder
        short_disease = db_entry["disease_name"]
        if db_entry["status"] == "Healthy":
            explanation_text = "The model analyzed the leaf surface and found uniform pigmentation and structural density, indicating a healthy plant tissue structure."
        else:
            explanation_text = f"The model focused on active regions in the leaf ({localization_text.split('leaf, ')[-1].replace('.', '')}), showing localized features characteristic of {short_disease}. The severity is estimated as {severity.upper()} based on the visual distribution of lesions."
            
        # Clean up memory explicitly
        del input_tensor
        del input_tensor_with_grad
        del logits
        del probs
        del cam_map
        import gc
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
        return {
            "plant_name": db_entry["plant_name"],
            "disease_name": db_entry["disease_name"],
            "status": db_entry["status"],
            "confidence": confidence,
            "severity": severity,
            "description": db_entry["description"],
            "symptoms": db_entry["symptoms"],
            "causes": db_entry["causes"],
            "prevention": db_entry["prevention"],
            "organic_remedies": db_entry["organic_remedies"],
            "chemical_remedies": db_entry["chemical_remedies"],
            "management_practices": db_entry["management_practices"],
            "explanation_text": explanation_text,
            "images": {
                "original": f"/static/uploads/{orig_filename}",
                "heatmap": f"/static/heatmaps/{heatmap_filename}",
                "overlay": f"/static/heatmaps/{overlay_filename}"
            }
        }
