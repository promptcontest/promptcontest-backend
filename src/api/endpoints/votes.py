from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from os import environ


router = APIRouter()


class Vote(BaseModel):
    image_id: int
    user_id: int


@router.post("/upvote")
async def post_upvote(vote: Vote):
    # result = supabase.table('upvotes').insert(vote.dict()).execute()
    # 
    # if result.error:
    #     raise HTTPException(status_code=400, detail=result.error.message)

    return {"detail": "Upvote successfully cast."}


@router.post("/downvote")
async def post_downvote(vote: Vote):
    # result = supabase.table('downvotes').insert(vote.dict()).execute()
    # 
    # if result.error:
    #     raise HTTPException(status_code=400, detail=result.error.message)

    return {"detail": "Downvote successfully cast."}