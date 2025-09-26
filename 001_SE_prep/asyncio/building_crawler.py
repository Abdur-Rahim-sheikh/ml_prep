import httpx
import asyncio


async def crawl0(prefix: str, url: str = "") -> None:
    url = url or prefix
    print(f"Crawling {url}")
    client = httpx.AsyncClient()

    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            await crawl0(prefix, line)


if __name__ == "__main__":
    asyncio.run(crawl0("https://langa.pl/crawl/"))
