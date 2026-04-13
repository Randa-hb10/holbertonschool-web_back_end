#!/usr/bin/env python3
"""This module provides a function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""

    def multiply(x: float) -> float:
        """Multiplies x by multiplier."""
        return x * multiplier

    return multiply
