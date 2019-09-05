# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def xprod(a, b):
    return ((_a, _b) for _a in a for _b in b)
