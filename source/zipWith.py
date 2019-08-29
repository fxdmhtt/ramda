# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def zipWith(fn, a, b):
    rv = []
    idx = 0
    len = min(len(a), len(b))
    while idx < len:
        rv.append(fn(a[idx], b[idx]))
        idx += 1
    return rv
