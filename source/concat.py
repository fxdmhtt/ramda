# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isArray import _isArray
from .internal._isFunction import _isFunction
from .internal._isString import _isString
from .toString import toString

@_curry2
def concat(a, b):
    if _isArray(a):
        if _isArray(b):
            return a.extend(b)
        raise TypeError(toString(b) + ' is not an array')
    if _isString(a):
        if _isString(b):
            return a + b
        raise TypeError(toString(b) + ' is not a string')
    if a is not None and _isFunction(a['fantasy-land/concat']):
        return a['fantasy-land/concat'](b)
    if a is not None and _isFunction(a.concat):
        return a.concat(b)
    raise TypeError(toString(a) + ' does not have a method named "concat" or "fantasy-land/concat"')
