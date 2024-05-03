#!/usr/bin/env python3
"""Takes a string and int or float and returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts Python variable to a Tuple."""
    return k, v ** 2
