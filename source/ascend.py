# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def ascend(fn, a, b):
    aa = fn(a)
    bb = fn(b)
    return (
        -1 if aa < bb
        else 1 if aa > bb
        else 0
    )
