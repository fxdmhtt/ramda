# -*- coding: utf-8 -*-

from ._isArray import _isArray
from ._isTransformer import _isTransformer

from . import sig
from . import _apply, JSObject

def _dispatchable(methodNames, xf, fn):
    from functools import wraps
    @wraps(fn)
    @sig
    def function(*arguments):
        if len(arguments) == 0:
            return fn()
        args = arguments[0:]
        *args, obj = args
        if not _isArray(obj):
            idx = 0
            while idx < len(methodNames):
                if callable(getattr(obj, methodNames[idx], None)):
                    return _apply(obj[methodNames[idx]], obj, args)
                idx += 1
            if _isTransformer(obj):
                transducer = _apply(xf, None, args)
                return transducer(obj)
        return _apply(fn, JSObject(), arguments)
    return function
