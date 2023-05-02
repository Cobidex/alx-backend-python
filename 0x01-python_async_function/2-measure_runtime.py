#!/usr/bin/env python3
'''
measure_time function
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n, and returns total_time / n

    Args:
        n (int): number of times to spawn wait_random.
        max_delay (int): max val of the random delay for each wait_random

    Returns:
        float: total execution time for wait_n(n, max_delay) divided by n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
