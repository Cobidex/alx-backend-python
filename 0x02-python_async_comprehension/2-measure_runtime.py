#!/usr/bin/env python3
'''
contains the measure_runtime function
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measures the runtime for async operations
    '''
    start = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
