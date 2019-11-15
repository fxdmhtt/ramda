# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def apply(fn, args):
    return fn(*args)
