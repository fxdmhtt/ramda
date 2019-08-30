# -*- coding: utf-8 -*-

from ._curry1 import _curry1
from ._curry2 import _curry2
from ._isPlaceholder import _isPlaceholder

def _curry3(fn):
    from functools import wraps
    @wraps(fn)
    def f3(*arguments):
        if len(arguments) == 0:
            return f3
        elif len(arguments) == 1:
            a, *_ = arguments
            return (
                f3 if _isPlaceholder(a)
                else _curry2(lambda _b, _c: fn(a, _b, _c))
            )
        elif len(arguments) == 2:
            a, b, *_ = arguments
            return (
                f3 if _isPlaceholder(a) and _isPlaceholder(b)
                else (
                    _curry2(lambda _a, _c: fn(_a, b, _c)) if _isPlaceholder(a)
                    else (
                        _curry2(lambda _b, _c: fn(a, _b, _c)) if _isPlaceholder(b)
                        else _curry1(lambda _c: fn(a, b, _c))
                    )
                )
            )
        else:
            a, b, c, *_ = arguments
            return (
                f3 if _isPlaceholder(a) and _isPlaceholder(b) and _isPlaceholder(c)
                else (
                    _curry2(lambda _a, _b: fn(_a, _b, c)) if _isPlaceholder(a) and _isPlaceholder(b)
                    else (
                        _curry2(lambda _a, _c: fn(_a, b, _c)) if _isPlaceholder(a) and _isPlaceholder(c)
                        else (
                            _curry2(lambda _b, _c: fn(a, _b, _c)) if _isPlaceholder(b) and _isPlaceholder(c)
                            else (
                                _curry1(lambda _a: fn(_a, b, c)) if _isPlaceholder(a)
                                else (
                                    _curry1(lambda _b: fn(a, _b, c)) if _isPlaceholder(b)
                                    else (
                                        _curry1(lambda _c: fn(a, b, _c)) if _isPlaceholder(c)
                                        else fn(a, b, c)
                                    )
                                )
                            )
                        )
                    )
                )
            )
    return f3
