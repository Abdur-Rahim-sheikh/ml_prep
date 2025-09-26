import asyncio
from typing import Coroutine, Callable
import time
import httpx
addr = "https://langa.pl/crawl/"

todo = set()
async def progress(
        url: str,
        algo: Callable[..., Coroutine]
)->None:
    asyncio.create_task(
        algo(url),
        name=url
    )

    todo.add(url)
    start = time.time()

    while len(todo):
        print(
            f"{len(todo)}: "
            + ", ".join(sorted(todo))[-38:]
        )
        await asyncio.sleep(0.5)
    end = time.time()
    print(f"Took {int(end - start)} Seconds")


async def crawl1(prefix: str, url: str = "") -> None:
    url = url or prefix

    client = httpx.AsyncClient()
    
    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            await crawl1(prefix, line)
    todo.discard(url)

async def crawl_faster(prefix: str, url: str = "") -> None:
    url = url or prefix

    client = httpx.AsyncClient()
    
    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            await crawl1(prefix, line)
    todo.discard(url)

if __name__ == "__main__":
    asyncio.run(progress(addr, crawl1))