#!/usr/bin/env python3
"""
contains the safe_first_element function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    return first element or none if an inputed iterable
    """
    if lst:
        return lst[0]
    else:
        return None
