import os
import string
import random

from fastapi import FastAPI, Depends
from pydantic import AnyUrl
import aioredis
from dotenv import load_dotenv

load_dotenv(".env")
app = FastAPI()
HOST_URL = os.getenv("SERVICE_HOSTNAME")
REDIS_URL = os.getenv("REDIS_URL")


async def session():
    return aioredis.from_url(REDIS_URL)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


@app.post("/long_url")
async def post_long_url(
    url: AnyUrl,
    session: aioredis.Redis = Depends(session)
):
    short_url_string = get_random_string(10)
    await session.set(short_url_string, url)
    return {"response": HOST_URL + short_url_string}


@app.get("/resolved_url/{url_id}")
async def get_resolved_url(
    url_id: str,
    session: aioredis.Redis = Depends(session)
):
    resolved_string = await session.get(url_id)
    return {"resolved": resolved_string}
