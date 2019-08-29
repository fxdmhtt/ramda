# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def and_(a, b):
    return a and b
