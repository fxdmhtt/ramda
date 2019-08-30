# -*- coding: utf-8 -*-

from ._isArray import _isArray
from ._isTransformer import _isTransformer

def _dispatchable(methodNames, xf, fn):
    from functools import wraps
    @wraps(fn)
    def function(*arguments):
        if len(arguments) == 0:
            return fn()
        args = arguments[0:]
        *args, obj = args
        if not _isArray(obj):
            idx = 0
            while idx < len(methodNames):
                if callable(getattr(obj, methodNames[idx], None)):
                    return obj[methodNames[idx]](*args)
                idx += 1
            if _isTransformer(obj):
                transducer = xf(*args)
                return transducer(obj)
        return fn(*arguments)
    return function
