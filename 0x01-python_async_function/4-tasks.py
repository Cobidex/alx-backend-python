#!/usr/bin/env python3
'''
contains the task_wait_n
'''
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    returns a list of delats
    '''
    delays = []
    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: delays.append(x.result()))
    await asyncio.gather(*[task_wait_random(max_delay) for i in range(n)])
    return delays
