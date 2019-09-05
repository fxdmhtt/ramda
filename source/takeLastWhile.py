# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .slice import slice

@_curry2
def takeLastWhile(fn, xs):
    idx = len(xs) - 1
    while idx >= 0 and fn(xs[idx]):
        idx -= 1
    return slice(idx + 1, None, xs)
