#!/usr/bin/env python3
"""Async coroutine measure_runtime"""
import asyncio
import random
from typing import List
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns runtime"""
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return (end - start)
