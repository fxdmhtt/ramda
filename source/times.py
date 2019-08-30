# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def times(fn, n):
    len_ = float(n)
    idx = 0

    import math
    if len_ < 0 or math.isnan(len_):
        raise ValueError('n must be a non-negative number')
    list = []
    while idx < len_:
        list.append(fn(idx))
        idx += 1
    return list
