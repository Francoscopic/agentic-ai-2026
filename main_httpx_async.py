import asyncio
import httpx

async def fetch_json(client, url):
    resp = await client.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()

async def main():
    urls = [
        "https://api.ipify.org?format=json",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*(fetch_json(client, u) for u in urls))
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())