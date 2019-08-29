# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def lt(a, b):
    return a < b
