# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce

@_curry1
def allPass(preds):
    def function(*arguments):
        idx = 0
        len_ = len(preds)
        while idx < len_:
            if not preds[idx](*arguments):
                return False
            idx += 1
        return True
    return curryN(reduce(max, 0, (pred.__code__.co_argcount for pred in preds)), function)
