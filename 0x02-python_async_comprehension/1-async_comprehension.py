#!/usr/bin/env python3
"""
This module contains the async_comprehension coroutine.
"""

from typing import List

# Import the async_generator function from the 0-async_generator module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async
    comprehending over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
