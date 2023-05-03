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
    return sorted([await task_wait_random(max_delay) for i in range(n)])
