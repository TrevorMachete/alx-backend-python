#!/usr/bin/env python3
"""
This module contains a function `safe_first_element` that takes a sequence
and returns the first element of the sequence if it exists,
otherwise it returns None.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    This function takes a sequence and returns the
    first element of the sequence if it exists,
    otherwise it returns None.

    Args:
        lst (Sequence[Any]): The sequence.

    Returns:
        Optional[Any]: The first element of the sequence
        if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element(["test", "example"]))
