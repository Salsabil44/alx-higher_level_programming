#!/usr/bin/python3
def magic_calculation(y, x, z):
    if y < x:
        return z
    elif z > x:
        return y + x
    return y * x - z
