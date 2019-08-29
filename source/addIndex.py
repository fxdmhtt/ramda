# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry1 import _curry1
from .curryN import curryN

@_curry1
def addIndex(fn):
    def function(*arguments):
        idx = 0
        origFn = arguments[0]
        list = arguments[len(arguments) - 1]
        args = arguments[0:]
        def function(*arguments):
            result = origFn(_concat(arguments, [idx, list]))
            idx += 1
            return result
        args[0] = function
        return fn(*args)
    return curryN(fn.__code__.co_argcount, function)
