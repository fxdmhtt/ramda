# -*- coding: utf-8 -*-

from ._curry1 import _curry1
from ._isPlaceholder import _isPlaceholder

def _curry2(fn):
    from .internal import undefined
    def f2(a=undefined, b=undefined):
        arguments = [a, b]
        while arguments and arguments[-1] is undefined:
            arguments.pop()

        if len(arguments) == 0:
            return f2
        elif len(arguments) == 1:
            a, *_ = arguments
            return (
                f2 if _isPlaceholder(a)
                else _curry1(lambda _b: fn(a, _b))
            )
        else:
            a, b, *_ = arguments
            return (
                f2 if _isPlaceholder(a) and _isPlaceholder(b)
                else (
                    _curry1(lambda _a: fn(_a, b)) if _isPlaceholder(a)
                    else (
                        _curry1(lambda _b: fn(a, _b)) if _isPlaceholder(b)
                        else fn(a, b)
                    )
                )
            )
    return f2
