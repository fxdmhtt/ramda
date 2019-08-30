# -*- coding: utf-8 -*-

from ._isPlaceholder import _isPlaceholder

def _curry1(fn):
    from .internal import undefined
    def f1(a=undefined):
        arguments = [a]
        while arguments and arguments[-1] is undefined:
            arguments.pop()

        if len(arguments) == 0:
            return f1
        else:
            a, *_ = arguments
            return (
                f1 if _isPlaceholder(a)
                else fn(a)
            )
    return f1
