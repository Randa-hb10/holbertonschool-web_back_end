#!/usr/bin/env python3
"""
This module contains an async function that runs multiple
wait_random coroutines concurrently and returns their delays.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of delays in ascending order.

    Args:
        n (int): Number of coroutines to run
        max_delay (int): Maximum delay

    Returns:
        List[float]: Sorted list of delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
