# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def xor(a, b):
    return bool((not a) ^ (not b))
