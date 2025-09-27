import asyncio
from typing import Awaitable


async def get_result(awaitable: Awaitable) -> str:
    try:
        result = await awaitable

    except Exception as e:
        print("Opps! ", e)
        return "No result :("
    else:
        return result
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    f = loop.create_future()

    
    loop.call_later(10, f.set_result, "This is my result")
    print(loop.run_until_complete(get_result(f)))

