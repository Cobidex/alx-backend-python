#!/usr/bin/env python3
'''
contains the make_multiplier function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    returns a function that multiplies a float by multiplier
    '''
    def multiply(n: float):
        '''
        multiply number by multiplier
        '''
        return n * multiplier
    return multiply
