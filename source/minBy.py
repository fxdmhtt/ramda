# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def minBy(f, a, b):
    return b if f(b) < f(a) else a
