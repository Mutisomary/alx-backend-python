#!/usr/bin/env python3
"""Variable annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """funtion to return a str and a float"""
    return (k, float(v) ** 2)
