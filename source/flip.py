# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN

@_curry1
def flip(fn):
    def function(a, b):
        args = arguments[0:]
        args[0] = b
        args[1] = a
        return fn(*args)
    from .internal import getArgCount
    return curryN(getArgCount(fn), function)
