#!/usr/bin/env python3
"""Funtion with annonated parameters that
returns values with the appropriate types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
