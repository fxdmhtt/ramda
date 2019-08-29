# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def until(pred, fn, init):
    val = init
    while not pred(val):
        val = fn(val)
    return val
