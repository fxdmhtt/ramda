# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce

from .internal import sig
from .internal import length
from .internal import jsify

@_curry1
def anyPass(preds):
    preds = [jsify(pred) for pred in preds]
    @sig
    def function(*arguments):
        idx = 0
        len_ = len(preds)
        while idx < len_:
            if preds[idx](*arguments):
                return True
            idx += 1
        return False
    return curryN(reduce(max, 0, (length(pred) for pred in preds)), function)
