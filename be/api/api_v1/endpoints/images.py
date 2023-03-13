import platform
from typing import Any, List
from uuid import uuid4
import torch
from diffusers import StableDiffusionPipeline

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.post("/generate",
             responses={
                 200: {
                     "content": {
                         "image/png": {},
                     },
                 }
             },
             response_class=StreamingResponse)
def txt2img(prompt: str):
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32)
    if "ARM64" in platform.version():
        pipe = pipe.to("mps")

    # pipe.enable_attention_slicing()
    pipe.safety_checker = lambda images, clip_input: (images, False)

    if "ARM64" in platform.version():
        _ = pipe(prompt, num_inference_steps=1)

    image = pipe(prompt, num_inference_steps=50).images[0]

    filename = uuid4()
    image.save(f"{filename}.png")

    file_image = open(f'{filename}.png', mode="rb")

    # Return the image as a stream specifying media type
    return StreamingResponse(content=file_image, media_type="image/png")
