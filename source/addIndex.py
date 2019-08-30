# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry1 import _curry1
from .curryN import curryN

@_curry1
def addIndex(fn):
    from functools import wraps
    @wraps(fn)
    def function(*arguments):
        idx = 0
        from .internal import wrapToJSFunction
        origFn = wrapToJSFunction(arguments[0])
        list_ = arguments[len(arguments) - 1]
        args = list(arguments[0:])
        def function(*arguments):
            nonlocal idx
            result = origFn(*_concat(arguments, [idx, list_]))
            idx += 1
            return result
        args[0] = function
        return fn(*args)
    from .internal import getArgCount
    return curryN(getArgCount(fn), function)
