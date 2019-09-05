# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isArray import _isArray
from .internal._isObject import _isObject
from .internal._isString import _isString

from .internal._getitem import _getitem

@_curry1
def empty(x):
    emptyFn = _getitem(x, 'empty')
    return (
        emptyFn() if callable(emptyFn)
        else [] if _isArray(x)
        else '' if _isString(x)
        else {} if _isObject(x)
        else None
    )
