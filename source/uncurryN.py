# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .curryN import curryN

from .internal import sig
from .internal import length

@_curry2
def uncurryN(depth, fn):
    @sig
    def function(*arguments):
        currentDepth = 1
        value = fn
        idx = 0
        while currentDepth <= depth and callable(value):
            endIdx = len(arguments) if currentDepth == depth else idx + length(value)
            value = value(*arguments[idx:endIdx])
            currentDepth += 1
            idx = endIdx
        return value
    return curryN(depth, function)
