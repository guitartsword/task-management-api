from fastapi import FastAPI

from api.main import api_router
from core import config


app = FastAPI()

app.include_router(api_router, prefix=config.PREFIX_V1)