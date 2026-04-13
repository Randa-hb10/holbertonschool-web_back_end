#!/usr/bin/env python3
"""
This module creates asyncio tasks from wait_random coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    that runs wait_random.

    Args:
        max_delay (int): Maximum delay

    Returns:
        asyncio.Task: The created task
    """
    return asyncio.create_task(wait_random(max_delay))
