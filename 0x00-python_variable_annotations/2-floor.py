#!/usr/bin/env python3
"""
This module contains a function `floor` that returns the floor of a float.
"""
import math


def floor(n: float) -> int:
    """
    This function returns the floor of a float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)


if __name__ == "__main__":
    print(floor(3.14))
