import asyncio


async def example(count: int) -> str:
    print("Before the first wait")
    await asyncio.sleep(0)

    if count == 0:
        print("Returning result")
        return "result"

    for i in range(count):
        print(f"Before await inside the loop iteration {i}")
        await asyncio.sleep(count - i)
        print(f"After await inside the loop iteration {i}")

    print(f"Before await on example {count - 1}")

    return await example(count - 1)


class TraceStep(asyncio.tasks._PyTask):
    def _Task__step(self, exc=None):
        print(f"<step(^) name={self.get_name()} done={self.done()}>")

        _ = super()._Task__step(exc=exc)
        print(f"</step name={self.get_name()} done={self.done()}>")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.set_task_factory(lambda loop, coro: TraceStep(coro, loop=loop))

    try:
        result = loop.run_until_complete(asyncio.gather(example(2), example(1)))
        print("Final result:", result)
    finally:
        loop.close()
