#!/usr/bin/env python3
"""Async basics"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Creating async coroutines by generating random numbers"""
    random_delay: float = random.uniform(0, max_delay)
    # wait for the random delay
    await asyncio.sleep(random_delay)
    # return the randomly generated delay
    return random_delay
