# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def times(fn, n):
    len = float(n)
    idx = 0

    import math
    if len < 0 or math.isnan(len):
        raise ValueError('n must be a non-negative number')
    list = []
    while idx < len:
        list.append(fn(idx))
        idx += 1
    return list
