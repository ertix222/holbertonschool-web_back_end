#!/usr/bin/env python3

"""Module that defines an asynchronous coroutine to wait a random time.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and the max_delay secondes.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
