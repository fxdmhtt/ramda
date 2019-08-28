# -*- coding: utf-8 -*-

import ._isPlaceholder import _isPlaceholder

def _curry1(fn):
    from functools import wraps
    @wraps(fn)
    def f1(*arguments):
        if len(arguments) == 0 or _isPlaceholder(arguments[0]):
            return f1
        else:
            return fn(*arguments)
    return f1
