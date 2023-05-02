#!/usr/bin/env python3
'''
contains task_wait_random
'''
import asyncio
from typing import TypeVar
wait_random = __import__('0-basic_async_syntax').wait_random
T = TypeVar('T')


def task_wait_random(max_delay: int) -> T:
    '''
    task_wait_random - regular function
    args:
        max_delay: an integer
    returns: asyncio.Task.
    '''
    task = asyncio.create_task(wait_random(max_delay))
    return task
