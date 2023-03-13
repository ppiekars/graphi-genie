from be.src.processing import generate_image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from celery.result import AsyncResult

router = APIRouter()


@router.post("/generate")
def txt2img(prompt: str):
    """Generate an image from a prompt"""
    filename = generate_image(prompt)

    file_image = open(f'{filename}.png', mode="rb")

    return StreamingResponse(content=file_image, media_type="image/png")


@router.post("/generate_celery")
def txt2img_celery(prompt: str):
    """Generate an image from a prompt using Celery"""
    task = generate_image.delay(prompt)
    return {"task_id": task.id}


@router.get("/generate/{task_id}")
def get_image(task_id: str):
    """Get the status of a task, return the image if it's done"""
    task = AsyncResult(task_id)
    print(task.status)
    if task.status == "SUCCESS":
        filename = task.result
        file_image = open(f'{filename}.png', mode="rb")
        return StreamingResponse(content=file_image, media_type="image/png")
    else:
        return {
            "task_id": task_id,
            "task_status": task.status,
        }

@router.post("/stop/{task_id}")
def stop_task(task_id: str):
    """Stop a running task"""
    AsyncResult(task_id).revoke(terminate=True)
    return {"task_id": task_id, "task_status": "REVOKED"}