#!/usr/bin/env python3
"""Async coroutine wait_n"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    lista = []
    for e in range (n):
        lista.append(await wait_random(max_delay))
    return lista
