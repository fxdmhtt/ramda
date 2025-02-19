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
            getattr(obj, methodname)(*arguments[0:length - 1]) if callable(getattr(obj, methodname, None))
            else obj[methodname](*arguments[0:length - 1]) if isinstance(obj, dict)
            else fn(*arguments)
        )
    return function
