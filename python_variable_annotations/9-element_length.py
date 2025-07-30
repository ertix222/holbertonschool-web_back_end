#!/usr/bin/env python3
"""This module defines a function that computes the length of each element
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element from the input iterable
    and its corresponding lenght.
    """
    return [(i, len(i)) for i in lst]
