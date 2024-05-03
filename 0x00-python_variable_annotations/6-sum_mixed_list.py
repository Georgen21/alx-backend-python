#!/usr/bin/env python3
"""Takes a mixed list of integers and floats then returns sum as a float"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Takes a mixed list of integers and floats then returns sum as a float"""
    return sum(mxd_list)
