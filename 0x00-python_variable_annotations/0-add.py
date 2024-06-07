#!/usr/bin/env python3
"""
This module contains a function `add` that adds two float numbers.
"""


def add(a: float, b: float) -> float:
    """
    This function adds two float numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":
    print(add(1.0, 2.0))
