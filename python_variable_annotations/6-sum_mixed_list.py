#!/usr/bin/env python3
"""  sum_mixed_list which takes a list mxd_lst of integers """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Accept a mixed list of integers and float and returns their sum as a float.
    """
    total_sum: float = 0.0
    for item in mxd_lst:
        total_sum += item
    return total_sum
