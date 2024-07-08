#!/usr/bin/env python3
'''
    Task 0
'''

from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    Delays the return of a random value for the duration of that value
    """
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
