#!/usr/bin/env python3
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the average execution time for wait_n(n, max_delay)"""

    # Record the start time
    start_time = time.time()

    # Call wait_n function to measure execution time
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the total execution time
    total_time = end_time - start_time

    # Calculate and return the average execution time per task
    return total_time / n
