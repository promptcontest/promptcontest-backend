import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from os import environ
from src.service.image_service import ImageService
from src.service.image_service import Image


router = APIRouter()


class ImageBody(BaseModel):
    user_id: str
    prompt: str
    twitter_handle: str
    image_url: str


@router.get("/images/{challenge_id}")
async def get_images(challenge_id: str):

    service = ImageService()
    result = service.get_challenge_images(challenge_id)

    return [x.to_dict() for x in result]


@router.post("/images/{challenge_id}/{user_id}")
async def submit_image(body: ImageBody, challenge_id: str, user_id: str):

    service = ImageService()

    if user_id != body.user_id:
        raise HTTPException(status_code=400, detail="User id mismatch")

    img = Image(user_id=body.user_id, prompt=body.prompt, twitter_handle=body.twitter_handle, image_url=body.image_url)

    result = service.add_image(challenge_id, img)

    return {'image_id': result.id}

