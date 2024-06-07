#!/usr/bin/env python3
"""
This module contains a function `safely_get_value` that
returns the value of a key in a dictionary
if it exists, otherwise it returns a default value.
"""

from typing import TypeVar, Dict

T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    """
    This function takes a dictionary, a key, and a default value,
    and returns the value of the key in the dictionary if it
    exists, otherwise it returns the default value.

    Args:
        dct (Dict[str, T]): The dictionary.
        key (str): The key.
        default (T, optional): The default value. Defaults to None.

    Returns:
        T: The value of the key in the dictionary if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    print(safely_get_value({"test": 1}, "test", 0))  # Outputs: 1
    print(safely_get_value({"test": 1}, "example", 0))  # Outputs: 0
