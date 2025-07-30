#!/usr/bin/env python3
"""This module defines a function that sums a list of integers and floats.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a tuple where the first element is the string 'k'
    """
    return (k, float(v ** 2))
