#!/usr/bin/env python3
"""Annotate function parameters return values with the types"""


def element_lenght(lst: List[str]) -> List[tuple[str, int]]:
    """Annotate function parameters return values with the types"""

    return [(i, len(i)) for i in lst]
