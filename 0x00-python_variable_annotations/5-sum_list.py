#!/usr/bin/env python3
"""
This module contains a function `sum_list` that sums a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function sums a list of floats.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)


if __name__ == "__main__":
    print(sum_list([1.0, 2.0, 3.0]))
