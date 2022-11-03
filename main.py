import os
import string
from random import choice

from fastapi import FastAPI, Depends
from pydantic import AnyUrl
import aioredis
from dotenv import load_dotenv

load_dotenv(".env")
app = FastAPI()
HOST_URL = os.getenv("HOSTNAME")
REDIS_URL = os.getenv("REDIS_URL")


def redis_session():
    url = REDIS_URL
    return aioredis.from_url(url)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


@app.post("/long_url")
async def post_long_url(
    url: AnyUrl,
    session: aioredis.Redis = Depends(redis_session)
):
    short_url_string = get_random_string(10)
    await session.set(short_url_string, url)
    return {"response": HOST_URL + short_url_string}


@app.get("/test")
async def test():
    return {"Okay": "200"}
