# Practice: Decorators, Async IO, Pydantic v2

Scaffolded exercises to drop into your `agentic-ai-2026` repo. Each file
has `TODO`s in place of the actual logic — fill them in, then run the
file directly to check your work.

## Setup

```bash
# from inside agentic-ai-2026/
uv add httpx pydantic requests
# or: pip install httpx pydantic requests
```

Copy these four files into your repo (e.g. under a `practice/` folder).

## Order to work through them

1. **`01_decorators.py`** — `@timer`, `@retry(times=3)`, `@log_args`,
   stacking decorators, a class-based decorator.
2. **`02_async_io.py`** — first coroutine, sequential vs concurrent
   timing, the "forgot to await" trap, concurrent `httpx` calls vs
   sequential `requests`, a producer/consumer queue, the blocking-call
   trap.
3. **`03_pydantic.py`** — `BaseModel` basics, `Field()` constraints,
   `@field_validator` (v2 syntax — not the deprecated `@validator`),
   nested models, `.model_dump()` / `.model_dump_json()`,
   `.model_validate()` on raw dict data.
4. **`04_fusion.py`** — combines all three: an async-aware retry
   decorator wraps an async function that fetches from a real public
   API and validates the response into a Pydantic model, run
   concurrently for multiple cities.

## Why this order

Decorators before async, because an async-compatible decorator (Part 4)
requires understanding plain decorators first — the wrapper function
itself has to become `async def` and use `await` internally, which is
confusing if decorators alone aren't solid yet.

Async before Pydantic, because Part 4's fetch function needs both at
once, and it's easier to trust your async code once you've already
proven it works with plain JSON responses (Part 2) before folding in
validation.

## Checking your work

Each file's `if __name__ == "__main__":` block runs every exercise in
order (uncomment lines in `02_async_io.py` as you implement each one).
Read the printed output and error messages carefully — in `03_pydantic.py`
especially, `e.errors()` on a caught `ValidationError` is worth reading
slowly; it tells you exactly which field failed and why, which is the
same structured error shape you'll see when an LLM's structured output
fails validation in LangChain/LangGraph.

## If you get stuck

Paste your attempt back and I'll review it — or ask for a hint on a
specific exercise number rather than the full solution, if you want to
keep wrestling with it a bit longer first.
