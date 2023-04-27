#!/usr/bin/env python3
'''
contains the element_length function
'''
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    returns a list of integer tupples
    '''
    return [(i, len(i)) for i in lst]
