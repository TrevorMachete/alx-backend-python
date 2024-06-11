#!/usr/bin/env python3
"""
0-basic_async_syntax.py
Module that defines a coroutine called wait_random
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Parameters:
    max_delay (Union[int, float]): Maximum delay

    Returns:
    float: Random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
