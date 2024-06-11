#!/usr/bin/env python3
"""
3-tasks.py
Module that defines a function called task_wait_random
"""

import asyncio
from typing import Callable

# Use __import__() to import the module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Callable:
    """
    Function that takes an integer max_delay and returns a asyncio.Task.

    Parameters:
    max_delay (int): Maximum delay

    Returns:
    Callable: asyncio.Task object
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
