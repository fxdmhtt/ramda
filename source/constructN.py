# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .curry import curry
from .nAry import nAry

@_curry2
def constructN(n, Fn):
    if n > 10:
        raise ValueError('Constructor with greater than ten arguments')
    if n == 0:
        return lambda: Fn()
    from .internal import undefined
    def function(a0=undefined, a1=undefined, a2=undefined, a3=undefined, a4=undefined, a5=undefined, a6=undefined, a7=undefined, a8=undefined, a9=undefined):
        arguments = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
        while arguments and arguments[-1] is undefined:
            arguments.pop()

        if len(arguments) == 1: return Fn(a0)
        if len(arguments) == 2: return Fn(a0, a1)
        if len(arguments) == 3: return Fn(a0, a1, a2)
        if len(arguments) == 4: return Fn(a0, a1, a2, a3)
        if len(arguments) == 5: return Fn(a0, a1, a2, a3, a4)
        if len(arguments) == 6: return Fn(a0, a1, a2, a3, a4, a5)
        if len(arguments) == 7: return Fn(a0, a1, a2, a3, a4, a5, a6)
        if len(arguments) == 8: return Fn(a0, a1, a2, a3, a4, a5, a6, a7)
        if len(arguments) == 9: return Fn(a0, a1, a2, a3, a4, a5, a6, a7, a8)
        if len(arguments) == 10: return Fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
    return curry(nAry(n, function))
