#!/usr/bin/env python3
"""
    Task 0
"""
from random import random
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate asynchronous coroutine
    """
    for i in range(10):
        await sleep(1)
        yield random() * 10
