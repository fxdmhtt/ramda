# -*- coding: utf-8 -*-

from ._isArray import _isArray

from . import sig
from . import _apply, JSObject

def _checkForMethod(methodname, fn):
    from functools import wraps
    @wraps(fn)
    @sig
    def function(*arguments):
        length = len(arguments)
        if length == 0:
            return fn()
        obj = arguments[length - 1]
        return (
            _apply(fn, JSObject(), arguments) if _isArray(obj) or not callable(getattr(obj, methodname, None))
            else _apply(obj[methodname], obj, arguments[0:length - 1])
        )
    return function
