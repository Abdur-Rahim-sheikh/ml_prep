import asyncio
from datetime import datetime


def print_now():
    print(datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.5)


async def async_main() -> None:
    try:
        gather_coroutine = asyncio.gather(
            keep_printing("First"), keep_printing("Second"), keep_printing("Third")
        )
        await asyncio.wait_for(
            gather_coroutine,
            5,
        )
    except asyncio.TimeoutError:
        print("Oops, time's up!")


async def async_main_wrong() -> None:
    # these three call are essentially synchrounous
    # though it will help if those functions are io bound, leaving
    # this process and work for ther job
    try:
        await keep_printing("First")
        await keep_printing("Second")
        await keep_printing("Third")

    except asyncio.TimeoutError:
        print("Oops, time's up!")


if __name__ == "__main__":
    asyncio.run(async_main())
    # asyncio.run(async_main_wrong())
