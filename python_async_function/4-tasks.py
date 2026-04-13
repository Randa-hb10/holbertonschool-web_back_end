#!/usr/bin/env python3
"""
This module runs multiple tasks concurrently using task_wait_random.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a list of delays in ascending order.

    Args:
        n (int): Number of tasks
        max_delay (int): Maximum delay

    Returns:
        List[float]: Sorted list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
