from typing import List, NoReturn
import asyncio
import time


async def write_async(array: List) -> NoReturn:
    """Q2 Function that writes every item with x second apart"""
    async def print_with_delay(delay, item):
        await asyncio.sleep(delay)
        print(item)
        print(f"printed at {time.strftime('%X')}")

    print(f"started at {time.strftime('%X')}")
    [await asyncio.create_task(print_with_delay(2**i, item)) for i, item in enumerate(array)]
    print(f"finished at {time.strftime('%X')}")
# asyncio.run(write_async(["a", "b", "c", "d"]))
