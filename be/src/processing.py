import platform
from uuid import uuid4
from celery import shared_task


@shared_task
def generate_image(prompt: str):
    """Generate an image from a prompt"""
    import torch
    from diffusers import StableDiffusionPipeline
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32)

    pipe.enable_attention_slicing()
    pipe.safety_checker = lambda images, clip_input: (images, False)

    image = pipe(prompt, num_inference_steps=50).images[0]

    filename = str(uuid4())
    image.save(f"{filename}.png")

    return filename