#!/usr/bin/env python3
"""
Task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a multiplier function
    """
    def f(n: float) -> float:
        """
        Multiplies a float
        """
        return float(n * multiplier)
    return f
