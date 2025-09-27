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
    task = asyncio.create_task(
        algo(url),
        name=url
    )

    todo.add(task)
    start = time.time()

    while len(todo):
        done, _pending = await asyncio.wait(
            todo,
            timeout=0.5
        )
        todo.difference_update(done)

        urls = (t.get_name() for t in todo)
        print(
            f"{len(todo)}: "
            + ", ".join(sorted(urls))[-75:]
        )
      
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
            
            task = asyncio.create_task(crawl_faster(prefix, line), name=line)
            todo.add(task)
    todo.discard(url)


async def async_main() -> None:
    try:
        await progress(addr, crawl_faster)
    except asyncio.CancelledError:
        for task in todo:
            task.cancel()
        
        done, pending = await asyncio.wait(todo, timeout=1.0)
        todo.difference_update(done)
        todo.difference_update(pending)

        if todo:
            print("warning, new tasks added while we were cancelling")


if __name__ == "__main__":
    # asyncio.run(progress(addr, crawl1))
    # asyncio.run(progress(addr, crawl_faster))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(async_main())
    loop.call_later(10, task.cancel)

    try:
        loop.run_until_complete(task)
    finally:
        loop.close()
    