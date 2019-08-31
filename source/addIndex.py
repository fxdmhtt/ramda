# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry1 import _curry1
from .curryN import curryN

from .internal import sig
from .internal import length
from .internal import jsify
from .internal import _apply, JSObject

@_curry1
def addIndex(fn):
    from functools import wraps
    @wraps(fn)
    @sig
    def function(*arguments):
        idx = 0
        origFn = jsify(arguments[0])
        list_ = arguments[len(arguments) - 1]
        args = list(arguments[0:])
        @sig
        def function(*arguments):
            nonlocal idx
            result = _apply(origFn, JSObject(), _concat(arguments, [idx, list_]))
            idx += 1
            return result
        args[0] = function
        return _apply(fn, JSObject(), args)
    return curryN(length(fn), function)
