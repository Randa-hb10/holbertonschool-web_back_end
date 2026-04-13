#!/usr/bin/env python3
"""This module provides a function that returns a key-value tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string and the square of the number."""
    return (k, float(v * v))
