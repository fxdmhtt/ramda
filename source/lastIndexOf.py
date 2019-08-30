# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isArray import _isArray
from .equals import equals

@_curry2
def lastIndexOf(target, xs):
    # ignore: native lastIndexOf

    idx = len(xs) - 1
    while idx >= 0:
        if equals(xs[idx], target):
            return idx
        idx -= 1
    return -1
