#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine.
"""

import asyncio
from time import time

# Import the async_comprehension function from the 1-async_comprehension module
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
        float: The total runtime.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()

    return end_time - start_time
