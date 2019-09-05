# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry1 import _curry1
from .curryN import curryN

from .internal import sig
from .internal import length
from .internal import jsify

@_curry1
def addIndex(fn):
    from functools import wraps
    @wraps(fn)
    @sig
    def function(*arguments):
        idx = 0
        origFn = jsify(arguments[0])
        list_ = arguments[-1]
        args = list(arguments)
        @sig
        def function(*arguments):
            nonlocal idx
            result = origFn(*_concat(arguments, [idx, list_]))
            idx += 1
            return result
        args[0] = function
        return fn(*args)
    return curryN(length(fn), function)
