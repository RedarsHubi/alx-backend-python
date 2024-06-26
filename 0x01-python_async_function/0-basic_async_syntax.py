#!/usr/bin/env python3
"""Async coroutine wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits random num and returns"""
    va = random.uniform(0, max_delay)
    await asyncio.sleep(va)
    return va
