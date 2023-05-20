from typing import Dict, List

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True

    PROJECT_NAME: str = "PromptContest"
    API_V1_STR: str = "/api/v1"

    HOST: str = '0.0.0.0'
    PORT: int = 8081

    class Config:
        env_prefix = 'PROMPT_CONTEST_'


settings = Settings()
