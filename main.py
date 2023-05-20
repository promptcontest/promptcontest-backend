import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.config import settings
from src.api.routes import routers

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # openapi_tags=settings.TAGS_METADATA
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(routers)


@app.get("/")
def read_root():
    return True


class EndpointFilter(logging.Filter):
    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = path

    def filter(self, record: logging.LogRecord) -> bool:
        if record.getMessage().find(" " + self._path + " ") == -1:
            return True

        return not record.getMessage().endswith("200")


uvicorn_logger = logging.getLogger("uvicorn.access")
uvicorn_logger.addFilter(EndpointFilter(path="/"))
uvicorn_logger.addFilter(EndpointFilter(path="/api/v1/health"))
uvicorn_logger.addFilter(EndpointFilter(path="/metrics"))


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.HOST,
        port=settings.PORT,
        # debug=settings.DEBUG,
        reload=settings.DEBUG
    )
