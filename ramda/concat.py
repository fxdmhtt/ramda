# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isArray import _isArray
from .internal._isFunction import _isFunction
from .internal._isString import _isString
from .toString import toString

from .internal._getitem import _getitem

@_curry2
def concat(a, b):
    if _isArray(a):
        if _isArray(b):
            return list(a) + list(b)
        raise TypeError(toString(b) + ' is not an array')
    if _isString(a):
        if _isString(b):
            return a + b
        raise TypeError(toString(b) + ' is not a string')
    concatFn = _getitem(a, 'concat')
    if _isFunction(concatFn):
        return concatFn(b)
    raise TypeError(toString(a) + ' does not have a method named "concat"')
