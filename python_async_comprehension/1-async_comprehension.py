#!/usr/bin/env python3
"""Module to asynchronously collect random numbers using async comprehension.
"""
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Asynchronously collects 10 random floats from async_generator.
    """
    result = [x async for x in async_generator()]
    return result