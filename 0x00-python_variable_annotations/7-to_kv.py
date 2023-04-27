#!/usr/bin/env python3
'''
contains the to_kv function
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    that takes a string k and an int OR float v
    as arguments and returns a tuple
    '''
    return (k, v**2)
