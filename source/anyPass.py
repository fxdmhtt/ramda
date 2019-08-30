# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce

@_curry1
def anyPass(preds):
    def function(*arguments):
        idx = 0
        len_ = len(preds)
        while idx < len_:
            if preds[idx](*arguments):
                return True
            idx += 1
        return False
    import inspect
    return curryN(reduce(max, 0, (len(inspect.signature(pred).parameters) for pred in preds)), function)
