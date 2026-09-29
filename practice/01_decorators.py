"""
Part 1 — Decorators
====================
Fill in each TODO. Run this file directly (`python 01_decorators.py`)
to check your work — expected output / hints are in the comments.

Why this matters: LangChain tools (`@tool`) and LangGraph nodes lean on
decorators to register your functions without you calling them directly.
Understanding what a decorator actually does removes the "magic".
"""

import functools
import time


# ---------------------------------------------------------------------------
# Exercise 1 — @timer
# ---------------------------------------------------------------------------
# Write a decorator that prints how long the wrapped function took to run.
# Use functools.wraps and be ready to explain WHY it's needed
# (hint: try removing it and check what happens to slow_add.__name__).

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: record start time
        # TODO: call func(*args, **kwargs) and store the result
        # TODO: record end time, print the elapsed duration
        # TODO: return the result
        raise NotImplementedError
    return wrapper


@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b


# ---------------------------------------------------------------------------
# Exercise 2 — @retry(times=3)  (a decorator FACTORY)
# ---------------------------------------------------------------------------
# This is one level deeper: retry(times=3) must itself return a decorator.
# retry(times=3)
#   -> returns `decorator`
#      decorator(func)
#        -> returns `wrapper`
#
# wrapper should call func, and if it raises an exception, retry up to
# `times` attempts before finally letting the exception propagate.

def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: loop up to `times` attempts
            # TODO: try calling func(*args, **kwargs); return on success
            # TODO: on exception, print which attempt failed, then continue
            # TODO: after the loop, if every attempt failed, re-raise
            raise NotImplementedError
        return wrapper
    return decorator


_attempt_counter = {"n": 0}


@retry(times=3)
def flaky():
    """Fails the first 2 times, succeeds on the 3rd — to prove retry works."""
    _attempt_counter["n"] += 1
    if _attempt_counter["n"] < 3:
        raise ValueError(f"simulated failure #{_attempt_counter['n']}")
    return "success!"


# ---------------------------------------------------------------------------
# Exercise 3 — @log_args
# ---------------------------------------------------------------------------
# Print the function name, its args/kwargs, and its return value every
# time it's called. Example print format is up to you, e.g.:
#   CALL greet(name='Joshua') -> 'Hello, Joshua'

def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: print call info before running func
        # TODO: call func, capture result
        # TODO: print result
        # TODO: return result
        raise NotImplementedError
    return wrapper


@log_args
def greet(name):
    return f"Hello, {name}"


# ---------------------------------------------------------------------------
# Exercise 4 — Stack two decorators, predict the order first
# ---------------------------------------------------------------------------
# Before running: write down (as a comment) what order you expect
# "timer" and "log_args" print statements to appear in, given the
# stacking order below. Then run it and check yourself.

# TODO: your prediction here as a comment

@timer
@log_args
def stacked_example(x):
    time.sleep(0.2)
    return x * 2


# ---------------------------------------------------------------------------
# Exercise 5 — Class-based decorator: @CountCalls
# ---------------------------------------------------------------------------
# Implement a decorator using a class with __init__ and __call__ instead
# of nested functions. It should track how many times the wrapped
# function has been called, accessible as `instance.count`.

class CountCalls:
    def __init__(self, func):
        # TODO: store func, initialize self.count = 0
        # TODO: functools.wraps doesn't work directly on class __init__;
        #       use functools.update_wrapper(self, func) instead
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        # TODO: increment self.count
        # TODO: call and return the wrapped function's result
        raise NotImplementedError


@CountCalls
def ping():
    return "pong"


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n--- Exercise 1: timer ---")
    print(slow_add(2, 3))

    print("\n--- Exercise 2: retry ---")
    print(flaky())

    print("\n--- Exercise 3: log_args ---")
    print(greet("Joshua"))

    print("\n--- Exercise 4: stacked decorators ---")
    print(stacked_example(5))

    print("\n--- Exercise 5: class-based decorator ---")
    ping()
    ping()
    ping()
    print(f"ping() was called {ping.count} times")
