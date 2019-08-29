# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def zip(a, b):
    rv = []
    idx = 0
    len = min(len(a), len(b))
    while idx < len:
        rv.append([a[idx], b[idx]])
        idx += 1
    return rv
