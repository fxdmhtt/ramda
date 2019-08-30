# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .curryN import curryN

@_curry2
def uncurryN(depth, fn):
    def function(*arguments):
        currentDepth = 1
        value = fn
        idx = 0
        while currentDepth <= depth and callable(value):
            endIdx = len(arguments) if currentDepth == depth else idx + value.__code__.co_argcount
            value = value(*arguments[idx:endIdx])
            currentDepth += 1
            idx = endIdx
        return value
    return curryN(depth, function)
