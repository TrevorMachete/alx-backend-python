#!/usr/bin/env python3
"""
This module contains a function `element_length` that takes a list of strings
and returns a list of tuples. Each tuple contains a string from the input list
and its length.
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    This function takes a list of strings and returns a list of tuples.
    Each tuple contains a string from the input list and its length.

    Args:
        lst (List[str]): The list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples.
        Each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length(["test", "example"]))
