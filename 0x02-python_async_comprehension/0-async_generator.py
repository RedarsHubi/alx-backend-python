#!/usr/bin/env python3
"""Async coroutine async_generator"""
import asyncio
import random
from typing import List


async def async_generator():
    """returns random list of floats"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
