#!/usr/bin/env python3
"""
    Task 1
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times
    """
    coros = [asyncio.create_task(wait_random(max_delay)) for task in range(n)]
    return [await coro for coro in asyncio.as_completed(coros)]
