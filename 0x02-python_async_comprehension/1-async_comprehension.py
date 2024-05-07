#!/usr/bin/env python3
"""Async coroutine async_generator"""
import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    lista = []
    async for e in async_generator():
        lista.append(e)
    return lista
