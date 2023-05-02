#!/usr/bin/env python3
'''
contains the coroutine wait_n
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    return the list of all the delays (float values)
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    my_list = await asyncio.gather(*tasks)
    return sorted(my_list)
