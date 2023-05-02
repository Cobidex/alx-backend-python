#!/usr/bin/env python3
'''
contains the coroutine wait_random
'''
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    '''
    waits for a random delay between 0 and max_delay 
    seconds and eventually returns it
    '''
    value = random.uniform(0, max_delay + 1)
    await asyncio.sleep(value)
    return value
