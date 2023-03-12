from typing import Any, List

from fastapi import APIRouter


router = APIRouter()


@router.post("/upload")
def upscale():
    pass