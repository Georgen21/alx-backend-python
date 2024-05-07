#!/usr/bin/env python3
""" Takes in two int arguments and spawns wait_random
n times with the specified max_delay. """

import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This function spawns wait_random n times with specified max_delay
    and returns list of all delays in ascending order. """
    delays = []
    tasks = []

    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
