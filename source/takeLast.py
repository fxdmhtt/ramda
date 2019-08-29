# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .drop import drop

@_curry2
def takeLast(n, xs):
    return drop(len(xs) - n if n >= 0 else 0, xs)
