# -*- coding: utf-8 -*-

from ._isPlaceholder import _isPlaceholder

def _curry1(fn):
    def f1(a=None):
        arguments = list(filter(lambda x: x is not None, [a]))
        if len(arguments) == 0:
            return f1
        else:
            a, *_ = arguments
            return (
                f1 if _isPlaceholder(a)
                else fn(a)
            )
    return f1
