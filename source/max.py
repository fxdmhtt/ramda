# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def max(a, b):
    return b if b > a else a
