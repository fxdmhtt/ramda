# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def comparator(pred):
    return lambda a, b: (
        -1 if pred(a, b)
        else 1 if pred(b, a)
        else 0
    )
