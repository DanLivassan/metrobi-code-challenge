from typing import List, NoReturn
import asyncio
import time

async def write_async(array: List) -> NoReturn:
    """Q2 Function that writes every item with x second apart"""
    async def print_with_delay(delay, item):
        start = time.time()
        await asyncio.sleep(delay)
        print(item)
        end = time.time()
        print("{:.2f}s from begining".format(end-start))
        print("-"*20)

    threads = [(print_with_delay(2**i, item)) for i, item in enumerate(array)]
    await asyncio.gather(*threads)
    
asyncio.run(write_async(["a", "b", "c", "d"]))
