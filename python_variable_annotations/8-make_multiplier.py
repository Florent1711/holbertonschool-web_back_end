#!/usr/bin/env python3
"""make_multiplier that takes a float multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    float multiplier as argument and returns multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
