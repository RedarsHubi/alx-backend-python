#!/usr/bin/env python3
"""Async func task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    preps = [task_wait_random(max_delay) for e in range(n)]
    return [await prep for prep in asyncio.as_completed(preps)]
