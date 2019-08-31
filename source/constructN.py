# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .curry import curry
from .nAry import nAry

from .internal import sig

@_curry2
def constructN(n, Fn):
    if n > 10:
        raise ValueError('Constructor with greater than ten arguments')
    if n == 0:
        return lambda *_: Fn()
    @sig(names=['$0', '$1', '$2', '$3', '$4', '$5', '$6', '$7', '$8', '$9'])
    def function(*arguments):
        if len(arguments) ==  1: return Fn(*arguments)
        if len(arguments) ==  2: return Fn(*arguments)
        if len(arguments) ==  3: return Fn(*arguments)
        if len(arguments) ==  4: return Fn(*arguments)
        if len(arguments) ==  5: return Fn(*arguments)
        if len(arguments) ==  6: return Fn(*arguments)
        if len(arguments) ==  7: return Fn(*arguments)
        if len(arguments) ==  8: return Fn(*arguments)
        if len(arguments) ==  9: return Fn(*arguments)
        if len(arguments) == 10: return Fn(*arguments)
    return curry(nAry(n, function))
