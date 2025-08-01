#!/usr/bin/env python3
"""Module to measure runtime of concurrent async comprehensions.
"""

import asyncio
import time
import typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime of four concurrent async_comprehension calls.
    """
    start_time: float = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time: float = time.time()
    return end_time - start_time
