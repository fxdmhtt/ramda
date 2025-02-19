# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isFunction import _isFunction
from .curryN import curryN
from .toString import toString

from .internal import sig

@_curry2
def invoker(arity, method):
    @sig
    def function(*arguments):
        target = arguments[arity]
        if _isFunction(getattr(target, method, None)):
            return getattr(target, method)(*arguments[0:arity])
        raise TypeError(toString(target) + ' does not have a method named "' + method + '"')
    return curryN(arity + 1, function)
