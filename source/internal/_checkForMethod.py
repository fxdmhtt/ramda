# -*- coding: utf-8 -*-

from ._isArray import _isArray

from . import sig

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
            fn(*arguments) if _isArray(obj) or not callable(getattr(obj, methodname, None))
            else obj[methodname](*arguments[0:length - 1])
        )
    return function
