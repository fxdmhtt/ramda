# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isFunction import _isFunction
from .curryN import curryN
from .toString import toString

from .internal import sig
from .internal import _apply

@_curry2
def invoker(arity, method):
    @sig
    def function(*arguments):
        target = arguments[arity]
        if target is not None and _isFunction(target[method]):
            return _apply(target[method], target, arguments[0:arity])
        raise TypeError(toString(target) + ' does not have a method named "' + method + '"')
    return curryN(arity + 1, function)
