import os

DATABASE_URL = os.environ["DATABASE_URL"]

# 60 minutes * 24 hours * 7 days = 7 days
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
PREFIX_V1 = "/api/v1"

SECRET_KEY: str = os.environ["SECRET_KEY"]
