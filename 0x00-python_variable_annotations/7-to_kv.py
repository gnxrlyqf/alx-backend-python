#!/usr/bin/env python3
'''
Task 7
'''
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Returns a tuple from a key-value pair
    '''
    return (k, v**2)
