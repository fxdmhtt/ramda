# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN

from .internal import sig
from .internal import length

@_curry1
def flip(fn):
    @sig(names=['a', 'b'])
    def function(*arguments):
        a, b, *_ = *arguments, None, None
        args = list(arguments)
        args[:2] = args[1::-1]
        return fn(*args)
    return curryN(length(fn), function)
