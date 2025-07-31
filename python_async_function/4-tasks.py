#!/usr/bin/env python3

"""Module that defines an async coroutine to run task_wait_random concurrently.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs task_wait_random n times concurrently
        and returns sorted list of delays.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
