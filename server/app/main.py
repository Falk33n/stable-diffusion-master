from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from diffusers import StableDiffusionPipeline
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from io import BytesIO

import torch
import os

load_dotenv()

CACHE_DIRECTORY = "D:\\huggingface_cache"

os.environ["HF_HOME"] = CACHE_DIRECTORY
os.environ["TRANSFORMERS_CACHE"] = CACHE_DIRECTORY
os.environ["HF_HUB_CACHE"] = CACHE_DIRECTORY

app = FastAPI()

FRONTEND_URL = os.getenv("SECRET_WEB_URL")

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

class ImageRequest(BaseModel):
    prompt: str = ""
    negative_prompt: str | None = None
    inference_steps: int = Field(..., ge=2, le=100)
    guidance_scale: float = Field(..., ge=0.0, le=10.0)

@app.post("/image-generator")
async def generate_image(request: ImageRequest):
    try:
        image = pipeline(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            num_inference_steps=request.inference_steps,
            guidance_scale=request.guidance_scale,
        ).images[0]

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)

        return StreamingResponse(
            buffered,
            media_type="image/png",
        )    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Stable Diffusion API is running!"}