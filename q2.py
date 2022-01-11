from typing import List, NoReturn
import asyncio
import time


async def write_async(array: List) -> NoReturn:
    """Q2 Function that writes every item with x second apart"""
    async def print_with_delay(delay, item):
        await asyncio.sleep(delay)
        print(item)

    print(f"started at {time.strftime('%X')}")
    threads = [(print_with_delay(2**i, item)) for i, item in enumerate(array)]
    await asyncio.gather(*threads)
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(write_async(["a", "b", "c", "d"]))
