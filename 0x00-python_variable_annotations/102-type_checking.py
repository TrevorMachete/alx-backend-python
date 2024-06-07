#!/usr/bin/env python3
"""
This module contains a function `zoom_array` that
takes a sequence and a factor, and returns a sequence
where each element is repeated factor times.
"""


from typing import TypeVar, Sequence, List

T = TypeVar('T')


def zoom_array(lst: Sequence[T], factor: int = 2) -> List[T]:
    """
    This function takes a sequence and a factor, and returns a sequence where
    each element is repeated factor times.

    Args:
        lst (Sequence[T]): The sequence.
        factor (int, optional): The factor. Defaults to 2.


    Returns:
        List[T]: A sequence where each element is repeated factor times.
    """
    zoomed_in: List[T] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    print(zoom_array([1, 2, 3], 2))
