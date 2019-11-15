# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from operator import sub
subtract = _curry2(sub)

@_curry2
def subtract(a, b):
    return a - b
