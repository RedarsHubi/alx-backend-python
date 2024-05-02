#!/usr/bin/env python3
"""Complex type function to_kv"""
from typing import List, Union


def to_kv(k: str, v: [Union[int, float]]) -> tuple[str, float]:
    """Takes string and int or float returns tuple"""
    return [k, v*v]
