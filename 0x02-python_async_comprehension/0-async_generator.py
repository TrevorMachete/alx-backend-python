#!/usr/bin/env python3
"""
This module contains the async_generator coroutine.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10 every second for 10 seconds.

    Returns:
        AsyncGenerator[float, None]: Yields a random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
