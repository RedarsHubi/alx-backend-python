#!/usr/bin/env python3
"""Async coroutine wait_n"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    preps = [asyncio.create_task(wait_random(max_delay)) for e in range (n)]
    return [await prep for prep in asyncio.as_completed(preps)]
