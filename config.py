import os
from dotenv import load_dotenv

load_dotenv() # reads .env into the process environment

API_KEY = os.getenv("EXAMPLE_API_KEY")

if not API_KEY:
    raise RuntimeError("EXAMPLE_API_KEY is not set - check your .env file")