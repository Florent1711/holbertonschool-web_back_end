#!/usr/bin/env python3
"""make_multiplier that takes a float multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Take float multiplier as a argment returns multiplies a float by multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
