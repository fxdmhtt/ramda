# -*- coding: utf-8 -*-

from ._isArray import _isArray
from ._isTransformer import _isTransformer

def _dispatchable(methodNames, xf, fn):
    from collections import Callable
    from functools import wraps
    @wraps(fn)
    def function(*arguments):
        if len(arguments) == 0:
            return fn()
        args = arguments[0:]
        obj = args.pop()
        if not _isArray(obj):
            idx = 0
            while idx < len(methodNames):
                if isinstance(obj[methodNames[idx]], Callable):
                    return obj[methodNames[idx]](args)
                idx += 1
            if _isTransformer(obj):
                transducer = xf(args)
                transducer(obj)
        return fn(*arguments)
    return function
