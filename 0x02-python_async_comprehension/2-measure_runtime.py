#!/usr/bin/env python3
"""
    Task 2
"""
from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Generate asynchronous coroutines and measure their runtime
    """
    begin = perf_counter()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    stop = perf_counter()
    return stop - begin
