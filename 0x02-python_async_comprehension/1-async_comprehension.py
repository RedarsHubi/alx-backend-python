#!/usr/bin/env python3
"""Async coroutine async_comprehension"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns 10 randoms nums"""
    return [i async for i in async_generator()]
