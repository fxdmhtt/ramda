# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN

from .internal import sig
from .internal import length

@_curry1
def flip(fn):
    @sig(names=['a', 'b'])
    def function(*arguments):
        a, b, *_ = arguments
        args = list(arguments[0:])
        args[0] = b
        args[1] = a
        return fn(*args)
    return curryN(length(fn), function)
