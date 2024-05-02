#!/usr/bin/env python3
"""Typed function sum_list"""


def sum_list(input_list: list) -> float:
    """Takes float list returns float"""
    sum: float = 0
    for e in input_list:
        sum += e
    return sum
