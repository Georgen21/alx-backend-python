#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect 10 random numbers using an async comprehension over
    async_generator and return 10 random numbers. """
    return [value async for value in async_generator()]
