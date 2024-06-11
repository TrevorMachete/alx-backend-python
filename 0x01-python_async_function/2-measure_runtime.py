#!/usr/bin/env python3
"""
2-measure_runtime.py
Module that defines a function called measure_time
"""

import asyncio
import time
from typing import List

# Use __import__() to import the module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Parameters:
    n (int): Number of times to spawn wait_random
    max_delay (int): Maximum delay

    Returns:
    float: Average time spent on wait_n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
