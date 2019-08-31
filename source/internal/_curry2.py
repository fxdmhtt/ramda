# -*- coding: utf-8 -*-

from ._curry1 import _curry1
from ._isPlaceholder import _isPlaceholder

from . import sig

def _curry2(fn):
    from functools import wraps
    @wraps(fn)
    @sig(names=['a', 'b'])
    def f2(*arguments):
        a, b, *_ = arguments
        if len(arguments) == 0:
            return f2
        elif len(arguments) == 1:
            return (
                f2 if _isPlaceholder(a)
                else _curry1(lambda _b: fn(a, _b))
            )
        else:
            return (
                f2 if _isPlaceholder(a) and _isPlaceholder(b)
                else _curry1(lambda _a: fn(_a, b)) if _isPlaceholder(a)
                else _curry1(lambda _b: fn(a, _b)) if _isPlaceholder(b)
                else fn(a, b)
            )
    return f2
