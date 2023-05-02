#!/usr/bin/env python3
'''
contains the coroutine wait_n
'''
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    return the list of all the delays (float values)
    '''
    my_list: List[float] = []
    for i in range(n):
        value = await wait_random(max_delay)
        my_list.append(value)
    return sorted(my_list)
