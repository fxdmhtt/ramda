# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xdropWhile import _xdropWhile
from .slice import slice

def dropWhile(pred, xs):
    idx = 0
    len_ = len(xs)
    while idx < len_ and pred(xs[idx]):
        idx += 1
    import sys
    return slice(idx, sys.maxsize, xs)
dropWhile = _curry2(_dispatchable(['dropWhile'], _xdropWhile, dropWhile))
