"""
Part 4 — Fusion exercise
=========================
The one that matters most: this shape (decorator + async fetch +
Pydantic validation + concurrent gather) is structurally close to what
a LangGraph tool node actually looks like.

Requires: httpx, pydantic
API used: https://wttr.in (no key needed, plain JSON weather data) —
if it's flaky, swap in any other public JSON weather API.
"""

import asyncio
import functools

import httpx
from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Step A — the model
# ---------------------------------------------------------------------------
# Define WeatherReport with fields that match what you'll pull out of the
# API response, e.g.:
#   city: str
#   temp_c: float
#
# You'll map the raw JSON onto these fields yourself in fetch_weather
# (the wttr.in JSON is nested, so you'll extract just what you need
# before constructing/validating the model — see TODOs below).

class WeatherReport(BaseModel):
    # TODO: city: str
    # TODO: temp_c: float
    pass


# ---------------------------------------------------------------------------
# Step B — an async-compatible retry decorator
# ---------------------------------------------------------------------------
# Bring your `retry` decorator from 01_decorators.py, but note: it needs
# to change to support wrapping an ASYNC function. The wrapper itself
# must be `async def`, and it must `await func(...)` inside, not just
# call it. Everything else (the retry-count loop, the try/except) stays
# conceptually the same.

def async_retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # TODO: loop up to `times` attempts
            # TODO: try: return await func(*args, **kwargs)
            # TODO: except Exception as e: print which attempt failed
            # TODO: after the loop, re-raise the last exception
            raise NotImplementedError
        return wrapper
    return decorator


# ---------------------------------------------------------------------------
# Step C — the async fetch + validate function
# ---------------------------------------------------------------------------
# Fetch current weather for a city from wttr.in in JSON format:
#   https://wttr.in/{city}?format=j1
# The response has a deeply nested structure; the field you want is
# typically response["current_condition"][0]["temp_C"].
# Wrap this function with @async_retry(times=3).

@async_retry(times=3)
async def fetch_weather(client: httpx.AsyncClient, city: str) -> WeatherReport:
    url = f"https://wttr.in/{city}?format=j1"
    # TODO: resp = await client.get(url, timeout=10)
    # TODO: resp.raise_for_status()
    # TODO: data = resp.json()
    # TODO: temp_c = float(data["current_condition"][0]["temp_C"])
    # TODO: return WeatherReport(city=city, temp_c=temp_c)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Step D — run it concurrently for multiple cities
# ---------------------------------------------------------------------------

CITIES = ["Abuja", "Lagos", "Nairobi"]


async def main():
    # TODO: open an httpx.AsyncClient() as `client`
    # TODO: asyncio.gather(*(fetch_weather(client, city) for city in CITIES))
    # TODO: print each validated WeatherReport
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())
