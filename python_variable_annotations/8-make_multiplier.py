#!/usr/bin/env python3
"""This module defines a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create and return a function that multiplies a float
        by the given multiplier.
    """
    def multiplier_fonction(m: float) -> float:
        """Multiply a float by the predefined multiplier.
        """
        return m * multiplier

    return multiplier_fonction
