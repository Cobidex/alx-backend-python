#!/usr/bin/env python3
'''
contains the safely_get_value function
'''
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, Any]:
    '''
    return values, add type annotations to the function
    '''
    if key in dct:
        return dct[key]
    else:
        return default
