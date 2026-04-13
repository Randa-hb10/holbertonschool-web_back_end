#!/usr/bin/env python3
"""This module provides a function to get elements and their lengths."""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
