# -*- coding: utf-8 -*-

from ._isPlaceholder import _isPlaceholder

from . import sig

def _curry1(fn):
    from functools import wraps
    @wraps(fn, updated=())
    @sig(names=['a'])
    def f1(*arguments):
        a, *_ = *arguments, None
        if len(arguments) == 0 or _isPlaceholder(a):
            return f1
        else:
            return fn(*arguments)
    return f1
