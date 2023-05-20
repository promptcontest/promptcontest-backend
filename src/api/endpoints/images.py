from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from os import environ


router = APIRouter()


class Image(BaseModel):
    id: int
    user_id: int
    twitter_handle: str
    image_url: str
    timestamp: str
    rank: int
    upvotes: int
    downvotes: int


@router.get("/images/{challenge_id}")
async def get_images(challenge_id: int):
    return {
        {
            'id': "prd-1",
            'image_url': 'https://storage.googleapis.com/pai-images/d20c2b0455ec4ac68757aaa8f3717b58.jpeg',
            'user_id': '123',
            'twitter_handle': 'jason',
            'rank': 1,
            'upvotes': 100,
            'downvotes': 1,
        },
        {
            'id': "prd-2",
            'image_url': 'https://pbs.twimg.com/profile_images/1590968738358079488/IY9Gx6Ok_400x400.jpg',
            'user_id': '123',
            'twitter_handle': 'elonmusk',
        }
    }
    # result = supabase.table('images').select().filter('challenge_id', 'eq', challenge_id).execute()
    #
    # if result.error or not result.data:
    #     raise HTTPException(status_code=400, detail=result.error.message if result.error else 'No images found for this challenge')
    #
    # images = [Image(**data) for data in result.data]
    # return images
