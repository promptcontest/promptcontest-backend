from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from os import environ


router = APIRouter()


class Image(BaseModel):
    id: int
    challenge_id: int
    user_id: int
    image_url: str
    timestamp: str


@router.get("/images/{challenge_id}")
async def get_images(challenge_id: int):
    return {}
    # result = supabase.table('images').select().filter('challenge_id', 'eq', challenge_id).execute()
    #
    # if result.error or not result.data:
    #     raise HTTPException(status_code=400, detail=result.error.message if result.error else 'No images found for this challenge')
    #
    # images = [Image(**data) for data in result.data]
    # return images
