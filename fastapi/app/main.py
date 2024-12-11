from diffusers import StableDiffusionPipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from io import BytesIO

import base64
import torch
import os

CACHE_DIRECTORY = "D:\\huggingface_cache"

os.environ["HF_HOME"] = CACHE_DIRECTORY
os.environ["TRANSFORMERS_CACHE"] = CACHE_DIRECTORY
os.environ["HF_HUB_CACHE"] = CACHE_DIRECTORY

app = FastAPI()

FRONTEND_URL = "localhost:5173"

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_NAME = "CompVis/stable-diffusion-v1-4"
DEVICE = "cpu"

def load_pipeline():
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_NAME,
            cache_dir=CACHE_DIRECTORY,
            torch_dtype=torch.float32,
        ).to(DEVICE)
        return pipe
    except Exception as error:
        raise RuntimeError(f"Failed to load the pipeline: {str(error)}")

pipeline = load_pipeline()  

DEFAULT_INFERENCE_STEPS = 50
DEFAULT_GUIDANCE_SCALE = 7.5

class ImageRequest(BaseModel):
    prompt: str
    inference_steps: int = DEFAULT_INFERENCE_STEPS
    guidance_scale: float = DEFAULT_GUIDANCE_SCALE

@app.post("/image-generator")
async def generate_image(request: ImageRequest):
    try:
        image = pipeline(
            prompt=request.prompt,
            num_inference_steps=request.inference_steps,
            guidance_scale=request.guidance_scale,
        ).images[0]

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return JSONResponse(content={"message": "Image generated successfully!", "image": img_str})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Stable Diffusion API is running!"}