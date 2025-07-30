#!/usr/bin/env python3
"""This module defines a function that returns a tuple
    with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is the string 'k'
    """
    return (k, v ** 2)
