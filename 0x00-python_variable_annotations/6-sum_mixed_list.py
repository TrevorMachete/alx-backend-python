#!/usr/bin/env python3
"""
This module contains a function `sum_mixed_list` that
sums a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function sums a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """

    return float(sum(mxd_lst))


if __name__ == "__main__":
    print(sum_mixed_list([1, 2.0, 3]))
