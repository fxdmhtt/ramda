# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce

@_curry1
def allPass(preds):
    from .internal import wrapToJSFunction
    preds = [wrapToJSFunction(pred) for pred in preds]
    def function(*arguments):
        idx = 0
        len_ = len(preds)
        while idx < len_:
            if not preds[idx](*arguments):
                return False
            idx += 1
        return True
    from .internal import getArgCount
    return curryN(reduce(max, 0, (getArgCount(pred) for pred in preds)), function)
