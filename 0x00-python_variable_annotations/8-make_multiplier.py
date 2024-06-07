#!/usr/bin/env python3
"""
This module contains a function `make_multiplier` that returns a function
that multiplies a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float as an argument and returns a function
    that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that
        multiplies a float by the multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func


if __name__ == "__main__":
    multiply_by_two = make_multiplier(2.0)
    print(multiply_by_two(3.0))  # Outputs: 6.0
