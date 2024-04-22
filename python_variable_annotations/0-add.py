#!/usr/bin/env python3
"""Fonction add annotée par type qui prend un  float a et b"""

def fact(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Un entier")
    if n < 0:
        raise ValueError("Un entier positif")
    result: int = 1
    while n > 1:
        result *= n
        n -= 1
    return result