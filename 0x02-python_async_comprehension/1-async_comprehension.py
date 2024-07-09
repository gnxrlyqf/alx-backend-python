#!/usr/bin/env python3
"""
    Task 1
"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """
    Generate asynchronous coroutines
    """
    return [task async for task in async_generator()]