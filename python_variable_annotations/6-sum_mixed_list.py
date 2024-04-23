#!/usr/bin/env python3
""" function sum_mixed_list which take list mxd_lst of int return their sum"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Accepts a mixed list of integers and floats and return their sum as float.
    """
    total_sum: float = 0.0
    for item in mxd_lst:
        total_sum += item
    return total_sum
