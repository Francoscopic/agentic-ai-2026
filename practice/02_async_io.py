"""
Part 2 — Async IO
==================
Based on the Real Python async IO guide (https://realpython.com/async-io-python/).
Run each exercise's block by setting RUN = <number> at the bottom, or just
run the whole file top to bottom.

Requires: httpx  (uv add httpx   OR   pip install httpx)

Why this matters: LangGraph nodes are frequently `async def`, and agent
frameworks run many tool/LLM calls concurrently with asyncio.gather().
"""

import asyncio
import time

import httpx


# ---------------------------------------------------------------------------
# Exercise 6 — Your first coroutine
# ---------------------------------------------------------------------------
# Write an async function that sleeps for 1 second (asyncio.sleep, NOT
# time.sleep) and then prints "done sleeping". Run it with asyncio.run().

async def first_coroutine():
    # TODO: await asyncio.sleep(1)
    # TODO: print("done sleeping")
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 7 — Sequential vs concurrent
# ---------------------------------------------------------------------------
# Below is a "slow" coroutine that simulates work. Write TWO runner
# functions:
#   run_sequential() — awaits slow_task() three times, one after another
#   run_concurrent()  — uses asyncio.gather() to run all three at once
# Time both with time.perf_counter() and compare the printed durations.
# Expect sequential ~= 3x concurrent.

async def slow_task(label, delay=1):
    await asyncio.sleep(delay)
    return f"{label} finished after {delay}s"


async def run_sequential():
    start = time.perf_counter()
    # TODO: await slow_task("A"), then slow_task("B"), then slow_task("C")
    #       in sequence, collecting results in a list
    raise NotImplementedError
    # elapsed = time.perf_counter() - start
    # print(f"Sequential took {elapsed:.2f}s -> {results}")


async def run_concurrent():
    start = time.perf_counter()
    # TODO: use asyncio.gather(slow_task("A"), slow_task("B"), slow_task("C"))
    raise NotImplementedError
    # elapsed = time.perf_counter() - start
    # print(f"Concurrent took {elapsed:.2f}s -> {results}")


# ---------------------------------------------------------------------------
# Exercise 8 — The "forgot to await" trap
# ---------------------------------------------------------------------------
# Call slow_task("oops") WITHOUT awaiting it inside this function.
# Run it and read the RuntimeWarning Python prints. Then fix it by adding
# `await`. Leave both the broken and fixed lines below (broken one
# commented out) so you can see the difference.

async def forgot_await_demo():
    # TODO (broken, then comment out): result = slow_task("oops")
    # TODO (fixed): result = await slow_task("oops")
    # print(result)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 9 — Concurrent HTTP calls with httpx vs sequential with requests
# ---------------------------------------------------------------------------
# Public JSON endpoints to hit (no API key needed):
URLS = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
    "https://jsonplaceholder.typicode.com/todos/5",
]


async def fetch_json(client: httpx.AsyncClient, url: str):
    # TODO: resp = await client.get(url, timeout=5)
    # TODO: resp.raise_for_status()
    # TODO: return resp.json()
    raise NotImplementedError


async def fetch_all_concurrent():
    start = time.perf_counter()
    # TODO: open an httpx.AsyncClient() as `client` (async with)
    # TODO: gather fetch_json(client, url) for every url in URLS
    raise NotImplementedError
    # elapsed = time.perf_counter() - start
    # print(f"httpx concurrent: {elapsed:.2f}s for {len(URLS)} requests")


def fetch_all_sequential_requests():
    """Compare against plain `requests`, one call at a time (sync)."""
    import requests
    start = time.perf_counter()
    results = []
    for url in URLS:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        results.append(resp.json())
    elapsed = time.perf_counter() - start
    print(f"requests sequential: {elapsed:.2f}s for {len(URLS)} requests")
    return results


# ---------------------------------------------------------------------------
# Exercise 10 — Producer/consumer with asyncio.Queue
# ---------------------------------------------------------------------------
# Build one producer coroutine that puts 5 numbered "jobs" onto an
# asyncio.Queue (with a small sleep between each, to simulate work
# arriving over time), and one consumer coroutine that pulls jobs off
# the queue and "processes" them (print + sleep) until it sees a
# sentinel value (e.g. None) telling it to stop.
#
# This models how agent pipelines pass work between steps.

async def producer(queue: asyncio.Queue):
    for i in range(5):
        # TODO: await asyncio.sleep(0.2)
        # TODO: await queue.put(f"job-{i}")
        pass
    # TODO: await queue.put(None)  # sentinel to signal "no more work"
    raise NotImplementedError


async def consumer(queue: asyncio.Queue):
    while True:
        # TODO: item = await queue.get()
        # TODO: if item is None: break
        # TODO: print(f"processing {item}")
        # TODO: await asyncio.sleep(0.1)
        raise NotImplementedError


async def run_producer_consumer():
    queue = asyncio.Queue()
    # TODO: await asyncio.gather(producer(queue), consumer(queue))
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 11 — The blocking-call trap
# ---------------------------------------------------------------------------
# Write an async function `bad_blocker()` that calls time.sleep(2)
# (NOT asyncio.sleep) inside an `async def`. Run it concurrently
# alongside a normal asyncio.sleep-based coroutine using gather(), and
# observe that the time.sleep() call freezes the ENTIRE event loop —
# the other coroutine doesn't get to run until the blocking call finishes.
# Write a one-line comment explaining why this happens.

async def bad_blocker():
    # TODO: time.sleep(2)  <-- note: NOT awaited, it's a blocking call
    raise NotImplementedError


async def well_behaved():
    for i in range(4):
        await asyncio.sleep(0.5)
        print(f"well_behaved tick {i}")


async def run_blocking_trap_demo():
    # TODO: asyncio.gather(bad_blocker(), well_behaved())
    # Expected (if you understand it correctly): well_behaved's ticks
    # should print WHILE bad_blocker sleeps, if things were truly async.
    # What actually happens with time.sleep() instead? Write your
    # observation as a comment here.
    raise NotImplementedError


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Uncomment exercises one at a time as you implement them.

    # asyncio.run(first_coroutine())

    # asyncio.run(run_sequential())
    # asyncio.run(run_concurrent())

    # asyncio.run(forgot_await_demo())

    # asyncio.run(fetch_all_concurrent())
    # fetch_all_sequential_requests()

    # asyncio.run(run_producer_consumer())

    # asyncio.run(run_blocking_trap_demo())

    pass
