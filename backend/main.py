# c:\Users\Kartik\Downloads\ntcc\plant-disease-app\backend\main.py

import os
# Limit threads to prevent memory explosion on multi-core hosts
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import torch
torch.set_num_threads(1)
torch.set_num_interop_threads(1)

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from PIL import Image
import io

from backend.predict import Predictor

app = FastAPI(
    title="AI Plant Disease Detection API",
    description="Production API for diagnosing plant leaf diseases with Grad-CAM++ explainability.",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resolve paths relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
WEIGHTS_PATH = os.path.join(BASE_DIR, "models", "best_model.pt")

# Create required folders
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(FRONTEND_DIR, exist_ok=True)

# Mount static files (uploads and heatmaps)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Mount frontend assets
app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")

# Serve PWA manifest and service worker from the root domain
@app.get("/manifest.json")
async def serve_manifest():
    return FileResponse(os.path.join(FRONTEND_DIR, "manifest.json"))

@app.get("/service-worker.js")
async def serve_service_worker():
    return FileResponse(os.path.join(FRONTEND_DIR, "service-worker.js"), media_type="application/javascript")

# Initialize Predictor lazily
predictor = None

def get_predictor():
    global predictor
    if predictor is None:
        if not os.path.exists(WEIGHTS_PATH):
            raise HTTPException(
                status_code=500,
                detail=f"Model weights file not found at {WEIGHTS_PATH}. Please make sure you have placed best_model.pt inside models/."
            )
        try:
            predictor = Predictor(weights_path=WEIGHTS_PATH, static_dir=STATIC_DIR)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to initialize AI model: {str(e)}"
            )
    return predictor

@app.on_event("startup")
async def startup_event():
    # Attempt to load model on startup to cache CUDA/CPU structures
    try:
        if os.path.exists(WEIGHTS_PATH):
            get_predictor()
            print("Successfully preloaded AI models and Grad-CAM hooks.")
        else:
            print(f"Warning: Weights not found at {WEIGHTS_PATH}. Model will load on first request after file is placed.")
    except Exception as e:
        print(f"Error during startup model loading: {e}")

@app.get("/")
async def serve_index():
    """Serve the landing page of the application."""
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Welcome to AI Plant Disease Detection API. Frontend index.html not found."}

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    """
    Accepts an uploaded image file, runs preprocessing and inference,
    generates Grad-CAM visual overlays, and returns a detailed treatment report.
    """
    # Verify file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be a valid image.")
        
    try:
        # Read image bytes
        image_data = await file.read()
        pil_image = Image.open(io.BytesIO(image_data)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")
        
    try:
        # Run prediction
        ai_predictor = get_predictor()
        result = ai_predictor.predict(pil_image)
        
        # Add a backward-compatible 'heatmap' parameter as requested by the API design
        result["heatmap"] = result["images"]["overlay"]
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/health")
async def health_check():
    """API health monitoring endpoint."""
    model_loaded = predictor is not None
    weights_present = os.path.exists(WEIGHTS_PATH)
    return {
        "status": "healthy",
        "model_loaded": model_loaded,
        "weights_present": weights_present,
        "device": predictor.device if model_loaded else "not_loaded"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
