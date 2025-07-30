#!/usr/bin/env python3

"""Module that defines an async coroutine to run wait_random concurrently.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs wait_random n times concurrently and returns sorted list of delays.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
