#!/usr/bin/env python3
"""
4-tasks.py
Module that defines a function called task_wait_n
"""

import asyncio
from typing import List

# Use __import__() to import the module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in 2 int arguments: n and max_delay.
    It spawns task_wait_random n times with the specified max_delay.

    Parameters:
    n (int): Number of times to spawn task_wait_random
    max_delay (int): Maximum delay

    Returns:
    List[float]: List of all the delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
