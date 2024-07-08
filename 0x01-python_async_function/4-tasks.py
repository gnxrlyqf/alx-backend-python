#!/usr/bin/env python3
"""
    Task 4
"""

from asyncio import as_completed
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times
    """
    coros = [task_wait_random(max_delay) for coro in range(n)]
    return [await coro for coro in as_completed(coros)]
