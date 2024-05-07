#!/usr/bin/env python3
"""
A measure_runtime coroutine that will execute async_comprehension four
times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Execute async_comprehension four times in parallel and
    measure the total runtime and return it. """
    first_time = time()
    await gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    end_time = time()

    return end_time - first_time
