#!/usr/bin/env python3
"""Async comprehensions"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Async Comprehensions"""
    # Record the start time
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    # Record the end time
    end_time = asyncio.get_event_loop().time()

    # Calculate the total runtime
    total_runtime = end_time - start_time

    return total_runtime
