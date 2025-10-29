from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import logging
from utils import convert_image_to_base64_and_test
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Leaf Disease Detection API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/disease-detection-file')
async def disease_detection_file(file: UploadFile = File(...)):
    try:
        logger.info("Received image file for disease detection")
        contents = await file.read()
        result = convert_image_to_base64_and_test(contents)
        if result is None:
            raise HTTPException(status_code=500, detail="Failed to process image file")
        return JSONResponse(content=result)
    except Exception as e:
        logger.error(f"Error in disease detection (file): {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/")
async def root():
    return {
        "message": "Leaf Disease Detection API",
        "version": "1.0.0",
        "endpoints": {
            "disease_detection_file": "/disease-detection-file (POST, file upload)"
        }
    }