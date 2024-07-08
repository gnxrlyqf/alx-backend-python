#!/usr/bin/env python3
"""
    Task 0
"""

# from random import random
# from asyncio import sleep
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Delays the return of a random value for the duration of that value
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
