from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from src.service.challenge_service import ChallengeService


router = APIRouter()


class Challenge(BaseModel):
    challenge: str


@router.get("/challenge")
async def get_current_challenge():

    service = ChallengeService()
    current_challenge = service.get_current_challenge()

    if current_challenge is None:
        return None

    return current_challenge


@router.post("/challenge/new")
async def post_new_challenge(body: Challenge):

        service = ChallengeService()
        new_challenge = service.create_new_challenge(name=body.challenge)

        if new_challenge is None:
            raise HTTPException(status_code=400, detail="Unable to create new challenge")

        return new_challenge
