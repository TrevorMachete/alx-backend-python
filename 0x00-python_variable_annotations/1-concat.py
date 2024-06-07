#!/usr/bin/env python3
"""
This module contains a function `concat` that concatenates two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    This function concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2


if __name__ == "__main__":
    print(concat("Hello, ", "World!"))
